from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from groq import Groq
import os
import json
import threading

# ============================================================
# STEP 1: CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)

# ============================================================
# STEP 2: LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY not found. Check your .env file."
    )

print("API key loaded successfully")

# ============================================================
# STEP 3: CREATE GROQ CLIENT
# ============================================================

client = Groq(api_key=api_key)

# ============================================================
# STEP 4: SYSTEM INSTRUCTIONS
# ============================================================

system_messages = [
    {
        "role": "system",
        "content": """
        You are an emotionally supportive AI friend.

        Rules:
        - Listen and understand emotions.
        - Give simple life advice.
        - Keep the conversation supportive and friendly.
        - Use previous conversation context when relevant.
        """
    }
]

# ============================================================
# STEP 5: LOAD CHAT HISTORY
# ============================================================

history_file = "chat_history.json"
history_lock = threading.Lock()

def load_history():
    if os.path.exists(history_file):
        try:
            with open(history_file, "r", encoding="utf-8") as file:
                saved_messages = json.load(file)

            # Keep only valid message dictionaries.
            if isinstance(saved_messages, list):
                saved_messages = [
                    item for item in saved_messages
                    if isinstance(item, dict)
                    and item.get("role") in ("system", "user", "assistant")
                    and isinstance(item.get("content"), str)
                ]
            else:
                saved_messages = []

        except (json.JSONDecodeError, OSError):
            saved_messages = []
    else:
        saved_messages = []

    # Ensure the system message is first.
    saved_messages = [
        item for item in saved_messages
        if item.get("role") != "system"
    ]

    return system_messages + saved_messages


messages = load_history()

# ============================================================
# STEP 6: SERVE SINGLE-FILE HTML
# ============================================================

@app.route("/")
def home():
    return send_from_directory(
        os.path.abspath("."),
        "index.html"
    )

# ============================================================
# STEP 7: CHAT API
# ============================================================

@app.route("/chat", methods=["POST"])
def chat():
    global messages

    data = request.get_json(silent=True) or {}
    prompt = data.get("message", "")

    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({
            "error": "Please enter a message."
        }), 400

    prompt = prompt.strip()

    # Protect shared conversation history from simultaneous writes.
    with history_lock:
        # Save previous history in case the API request fails.
        previous_messages = messages.copy()

        messages.append({
            "role": "user",
            "content": prompt
        })

        try:
            # Use the same recent-message approach as your chatbot.
            recent_messages = (
                system_messages + messages[1:][-10:]
            )

            # Request a response from Groq.
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=recent_messages,
                stream=False,
                include_reasoning=False
            )

            answer = response.choices[0].message.content

            if not answer:
                raise RuntimeError("The AI returned an empty response.")

            # Save assistant response.
            messages.append({
                "role": "assistant",
                "content": answer
            })

            # Persist conversation history.
            with open(history_file, "w", encoding="utf-8") as file:
                json.dump(messages, file, indent=4)

            return jsonify({
                "response": answer
            })

        except Exception:
            # Remove the failed request from in-memory history.
            messages = previous_messages

            app.logger.exception("Chat request failed")

            return jsonify({
                "error": "Unable to generate a response. Check the Flask terminal for details."
            }), 500

# ============================================================
# STEP 8: RUN FLASK SERVER
# ============================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
