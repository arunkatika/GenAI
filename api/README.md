# 🧠 LangChain Essay & Poem Generator

This project demonstrates how to build an AI-powered API service using **LangChain**, **FastAPI**, and **Streamlit**, with support for both cloud (OpenAI) and local (Ollama LLaMA2) LLMs.

---

## ✨ Features

- 📝 **Essay Generator** using OpenAI GPT (via LangChain)
- 🧸 **Poem Generator** using Ollama LLaMA2 (offline)
- 🌐 FastAPI server with LangServe for serving chains
- 🎨 Interactive Streamlit frontend for input/output
- 🔄 Supports both cloud-based and local LLM workflows

---

## 🗂️ Project Structure

```
├── app.py           # FastAPI server with LangServe routes
├── client.py        # Streamlit UI for interacting with essay/poem generators
├── .env             # Contains OpenAI API Key
├── requirements.txt # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/langchain-essay-poem-generator.git
cd langchain-essay-poem-generator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set OpenAI API Key
Create a `.env` file:
```
OPENAI_API_KEY=your-openai-key
```

### 5. Start FastAPI Backend
```bash
python app.py
```
This will run the backend server at `http://localhost:8000`.

### 6. Launch Streamlit Frontend
```bash
streamlit run client.py
```

---

## 🔍 API Endpoints

- `POST /essay/invoke` → Generates a 100-word essay using OpenAI
- `POST /poem/invoke` → Generates a 100-word poem using LLaMA2

---

## 📦 Dependencies

- `fastapi`
- `uvicorn`
- `langchain`
- `langserve`
- `langchain-community`
- `langchain-openai`
- `streamlit`
- `requests`
- `python-dotenv`
- `ollama` (for local model support)

---

## 📸 Demo Screenshot

![screenshot](![image](https://github.com/user-attachments/assets/807bf933-3bba-4cdd-a5c1-38996f9d2d58)
) <!-- optional -->

---

## 🧠 Credits

Created using:
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [OpenAI GPT](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)

---

