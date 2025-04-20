# 🤖 GenAI Chatbot Demos

This repo contains two LangChain-based chatbot apps built with Streamlit:

1. **app.py** – Uses `OpenAI GPT-3.5-Turbo` via OpenAI API  
2. **localama.py** – Uses `LLaMA3` via `Ollama` locally (no internet required)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/genai-chatbots.git
   cd genai-chatbots
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 Environment Setup

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Make sure to load the `.env` file at runtime (already done in the code via `dotenv`).

---

## 🚀 Running the Apps

### 1. OpenAI-based Chatbot

```bash
streamlit run app.py
```

- Requires internet
- Uses OpenAI's GPT-3.5 Turbo
- Quota and billing needed

### 2. Ollama-based Local Chatbot

```bash
ollama run llama3
streamlit run localama.py
```

- Works **offline**
- Requires [Ollama](https://ollama.com) installed
- Faster for local development

---

## 📁 Project Structure

```bash
.
├── app.py           # OpenAI-based chatbot
├── localama.py      # LLaMA3 (Ollama) based local chatbot
├── .env             # Store your API keys here
├── requirements.txt
└── README.md
```

---

## 📬 Contact

If you find this helpful or want to collaborate on GenAI tools, feel free to reach out or fork and star the repo!
