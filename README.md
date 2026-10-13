# 🤗 AI Friend Chatbot

An emotionally supportive AI chatbot built with **Python, Flask, Groq API, and HTML/CSS/JavaScript**. The chatbot is designed to provide friendly, empathetic, and encouraging conversations through a simple web interface.

## ✨ Features

- 💬 **AI-powered conversations** — Generate responses using the Groq API.
- ❤️ **Emotionally supportive responses** — Designed to respond with empathy and encouragement.
- 🌐 **Web-based interface** — Chat through a clean HTML, CSS, and JavaScript frontend.
- 💾 **Chat history persistence** — Save conversations locally in a JSON file.
- 🗑️ **Clear chat functionality** — Reset saved conversation history.
- 🔒 **Environment-based API key** — Store your Groq API key in a `.env` file.
- 🐍 **Flask backend** — Handle chat requests and conversation management.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web server and API routes |
| Groq API | AI-generated responses |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Chat interface interactions |
| JSON | Local conversation history |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
ai-friend-chatbot/
├── app.py
├── chatbot.py
├── index.html
├── .env
├── .gitignore
├── chat_history.json
├── README.md
└── .venv/
```

**Note:** `.env`, `chat_history.json`, and `.venv/` are local files or folders and should not be committed to GitHub. The structure above illustrates the development environment, not the files that should all be uploaded.

## ⚙️ Prerequisites

Before running the application, install:

- Python 3.10 or later
- A Groq API key
- Git (optional, for version control)

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-friend-chatbot.git
cd ai-friend-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask groq python-dotenv
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key. Never publish your API key or commit your `.env` file to GitHub.

### 5. Run the application

```bash
python app.py
```

Open your browser and navigate to:

**http://127.0.0.1:5000**

You can now interact with your AI friend through the web interface.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the chatbot web interface |
| POST | `/chat` | Sends a message to the AI chatbot |
| POST | `/clear` | Clears the saved conversation history |

### Example chat request

```json
{
  "message": "I'm feeling stressed today."
}
```

### Example response

```json
{
  "success": true,
  "response": "I'm sorry today has been stressful. Would you like to talk about what's been happening?"
}
```

The actual response will vary depending on the conversation and AI model output.

## 💾 Chat History

Conversation history is stored locally in `chat_history.json` so that messages can persist across application restarts.

The Clear Chat feature resets the saved conversation while preserving the chatbot's system instructions.

## 🔐 Security Notes

- Never upload your `.env` file or expose your Groq API key.
- Keep `.venv/` out of version control.
- Avoid publishing personal conversations from `chat_history.json`.
- Do not use Flask's debug server as a production deployment server.
- Consider adding authentication and request rate limiting before making the chatbot publicly accessible.

## 🔮 Future Improvements

- Streaming AI responses
- User authentication and individual chat histories
- Improved conversation memory
- Dark and light themes
- Voice input and text-to-speech
- Deployment to a cloud hosting platform
- Additional safeguards and privacy controls

## 🎯 Project Objective

The goal of this project is to build an accessible AI companion that provides supportive conversations through a web application while demonstrating the integration of Python, Flask, an AI API, and frontend web technologies.

## 📄 License

This project is available for learning and personal development. Add a specific open-source license, such as the MIT License, if you want to define permissions for reuse and distribution.

---

**Developed with Python, Flask, and Groq.** ❤️
