# 🎓 AI Study Bot  
Context-Aware Academic Chatbot using FastAPI, Groq LLM & MongoDB

---

## 📌 Project Overview

AI Study Bot is an intelligent academic chatbot that answers study-related questions using a Large Language Model (Groq LLM).

The system maintains conversation memory using MongoDB Atlas, allowing contextual follow-up responses.  
The backend is built with FastAPI and deployed live on Render.

---

## 🚀 Features

- 📚 Answers academic & technical questions
- 🧠 Context-aware memory using MongoDB
- ⚡ FastAPI REST API backend
- 🌍 Live cloud deployment (Render)
- 💻 Terminal-based chat interface
- 🔄 Supports follow-up contextual questions

---

## 🛠 Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Groq LLM
- LangChain
- MongoDB Atlas
- Render (Cloud Hosting)
- GitHub

---

## 🏗 System Architecture

User → FastAPI → Groq LLM  
      ↓  
    MongoDB (Chat History Storage)

### Workflow:
1. User sends question
2. Chat history retrieved from MongoDB
3. History passed to Groq LLM
4. LLM generates contextual response
5. Conversation stored in database

---

## 📡 API Endpoint

### 🔹 POST `/chat`

### Example Request:

```json
{
  "user_id": "render_user",
  "question": "What is recursion?"
}
```

### Example Response:

```json
{
  "response": "Recursion is a way of solving a problem by letting a function call itself..."
}
```

---

## 🌍 Live Deployment

🔗 https://study-bot-lxby.onrender.com/docs

---

## 💾 Memory Implementation

Each conversation message is stored with:
- `user_id`
- `role` (user / assistant)
- `message`
- `timestamp`

Before generating a response, previous chat history is retrieved and passed to the LLM, enabling contextual and intelligent follow-up answers.

---

# 📸 Project Screenshots

---

## 🌍 Deployment (Render)
![Render Logs](screenshot-5.png)
![Render Live](screenshot-6.png)

---

## 📡 FastAPI Swagger Testing
![Swagger Question 1](screenshot-1.png)
![Swagger Response 1](screenshot-2.png)
![Swagger Question 2](screenshot-3.png)
![Swagger Response 2](screenshot-4.png)

---

## 🧠 MongoDB Chat Storage
![MongoDB 1](screenshot-7.png)
![MongoDB 2](screenshot-8.png)

---

## 💻 Terminal Chat Demo
![Terminal Chat](screenshot-9.png)

---

## ▶ Run Locally

1. Clone repository:
```bash
git clone https://github.com/yourusername/study-bot.git
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```
GROQ_API_KEY=your_groq_key
MONGODB_URI=your_mongodb_uri
```

5. Run server:
```bash
python -m uvicorn main:app --reload
```

6. Open:
```
http://127.0.0.1:8000/docs
```
