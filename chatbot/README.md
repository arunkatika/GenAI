# 🤖 GenAI Chatbot Demos

This repository showcases two chatbot applications built with **LangChain** and **Streamlit** — designed to demonstrate both cloud-based and fully local conversational AI.
![image](https://github.com/user-attachments/assets/ffd681b4-c655-4b4d-b63b-134bbdb9ce9e)

### 🔹 What It Does

The project features two interactive chatbots:

1. **OpenAI Chatbot (`app.py`)**
   - Uses **GPT-3.5-Turbo** via OpenAI API
   - Requires internet and API key
   - Ideal for production-grade LLM access

2. **Local LLaMA Chatbot (`localama.py`)**
   - Uses **LLaMA3** via **Ollama**
   - Runs fully **offline**
   - Great for local development and testing without API costs

---

## ⚙️ Installation Steps

```bash
git clone https://github.com/arunkatika/GenAI.git
cd chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Create a `.env` file with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

Both `app.py` and `localama.py` will auto-load this via `dotenv`.

---

## 🚀 Running the Chatbots

### 🌐 OpenAI-Powered Chatbot

```bash
streamlit run app.py
```

- Uses GPT-3.5-Turbo from OpenAI
- Requires valid OpenAI and LangChain API keys
- Needs internet access

### 🖥️ Local LLaMA3 Chatbot

```bash
ollama run llama3
streamlit run localama.py
```

- Works offline using the Ollama runtime
- Fast and free to use locally

---

## 🗂️ Project Structure

```
.
├── app.py           # OpenAI chatbot with GPT-3.5-Turbo
├── localama.py      # Offline chatbot using LLaMA3 via Ollama
├── .env             # API keys (excluded from Git)
├── requirements.txt # Python dependencies
└── README.md
```

---

## 🤝 Connect

Found this useful? Feel free to fork, star 🌟 the repo, or reach out to collaborate on future GenAI projects!
