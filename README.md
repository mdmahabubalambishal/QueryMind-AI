---

title: QueryMind-AI
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: "1.42.0"
python_version: "3.10"
app_file: app.py
pinned: false

---

# 🤖 AI Research Assistant

একটি intelligent research assistant যা LangGraph, Groq, এবং Streamlit দিয়ে তৈরি। যেকোনো বিষয়ে web search, Wikipedia, এবং document analysis করে বাংলা বা English এ বিস্তারিত উত্তর দেয়।

---

## ✨ Features

- 🔍 **Web Search** — DuckDuckGo দিয়ে real-time web search
- 📖 **Wikipedia Search** — যেকোনো বিষয়ে বিস্তারিত তথ্য
- 📄 **File Upload** — PDF বা TXT file upload করে analyze
- 🌐 **Multi-language** — Bengali ও English এ উত্তর
- ⚡ **Streaming Response** — টাইপ হতে দেখা যায়
- 💾 **Chat History** — conversation save ও load করা যায়
- 📥 **PDF Export** — পুরো chat PDF এ export করা যায়
- 📋 **Copy Button** — যেকোনো response copy করা যায়

---

## 🛠️ Tech Stack

| Technology | ব্যবহার |
|------------|---------|
| **LangGraph** | AI Agent framework |
| **LangChain** | LLM tools ও utilities |
| **Groq** | LLM API (LLaMA 3.3 70B) |
| **Streamlit** | Web UI |
| **DuckDuckGo** | Web search |
| **Wikipedia API** | Knowledge base |
| **Python** | Backend language |

---

## 📁 Project Structure
```
research_agent/
│
├── .env                  # API keys
├── requirements.txt      # Python dependencies
├── tools.py             # LangChain tools (search, wikipedia)
├── agent.py             # LangGraph agent setup
├── app.py               # Streamlit UI
├── chat_history.json    # Saved chat history (auto-generated)
└── README.md            # Project documentation
```

---

### 1. Installation

### 2. Virtual environment তৈরি করো
```bash
python -m venv venv

# Windows
venv\Scripts\activate

### 3. Dependencies install করো
```bash
pip install -r requirements.txt
```

### 4. API Key সেট করো
`.env` file তৈরি করো:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run করো
```bash
streamlit run app.py
```

Browser এ যাও: `http://localhost:8501`

---

## 🚀 ব্যবহার করার নিয়ম

### Web Search
```
LangGraph কী এবং কীভাবে কাজ করে?
২০২৫ সালে AI এর নতুন developments কী কী?
```

### Wikipedia Search
```
Artificial Intelligence এর ইতিহাস বলো
Bangladesh এর অর্থনীতি সম্পর্কে বিস্তারিত বলো
```

### File Upload
```
১. Sidebar এ PDF বা TXT file upload করো
২. প্রশ্ন করো: "এই document এর মূল বিষয় কী?"
```

### Language Switch
```
Sidebar এ Bengali 🇧🇩 বা English 🇬🇧 select করো
```

---


## 📈 Future Improvements

- [ ] Voice input (Whisper API)
- [ ] Image generation tool
- [ ] Database memory (long-term)
- [ ] Multi-agent collaboration
- [ ] Deploy to cloud (Streamlit Cloud / HuggingFace Spaces)

---

## 👨‍💻 Author

**Mahabub**
- Junior AI Engineer (Learning)
- Focus: LLM Engineering, AI Agents, RAG, Prompt Engineering

---
