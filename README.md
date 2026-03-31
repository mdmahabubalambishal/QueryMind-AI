---
title: Autonomous Research Agent
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
license: mit
---

<div align="center">

# 🧠 Autonomous Research Agent

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=667EEA&center=true&vCenter=true&width=600&lines=Intelligent+AI+Research+Assistant;LangGraph+%7C+Groq+%7C+Streamlit;Web+Search+%7C+Wikipedia+%7C+PDF+Analysis;Bengali+%F0%9F%87%A7%F0%9F%87%A9+%7C+English+%F0%9F%87%AC%F0%9F%87%A7+Support" alt="Typing SVG" />

<br>

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-ReAct_Agent-FF6B6B?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F54E42?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-Deployed-FFD21E?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2ecc71?style=for-the-badge)

<br>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-FF4B4B?style=for-the-badge)](https://huggingface.co/spaces/mahabub-unlocked/QueryMind-AI)
[![LinkedIn](https://img.shields.io/badge/👤_Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/md-mahabub-alam-bishal/)

<br>

> **একটা intelligent AI research assistant যা যেকোনো বিষয়ে real-time web search, Wikipedia analysis, এবং document processing করে বিস্তারিত উত্তর প্রদান করে — LangGraph এর ReAct agent framework দিয়ে।**

</div>

---

## 🎯 Project Overview

Autonomous Research Agent হল একটি AI-powered research assistant যা তিনটা powerful tool ব্যবহার করে —

**Web Search** — DuckDuckGo দিয়ে real-time internet search  
**Wikipedia Analysis** — যেকোনো বিষয়ে Wikipedia থেকে বিস্তারিত তথ্য  
**Document Processing** — PDF ও TXT file upload করে analyze করা  

---

## 🚀 Live Demo

**👉 [App Open করো](https://huggingface.co/spaces/mahabub-unlocked/QueryMind-AI)**

| Feature | Description |
|---------|-------------|
| 🔍 Web Search | Real-time internet search |
| 📖 Wikipedia | বিস্তারিত research |
| 📄 File Analysis | PDF ও TXT analyze |
| 🌐 Multilingual | Bengali ও English support |
| ⚡ Streaming | Real-time typing effect |

---

## 🏗️ Architecture
```
User Query (Bengali / English)
        │
        ▼
┌───────────────────┐
│   ReAct Agent     │ ── Tool selection decision
│   (LangGraph)     │
└────────┬──────────┘
         │
    ┌────┴────┐
    ▼         ▼         ▼
┌────────┐ ┌────────┐ ┌────────┐
│  Web   │ │ Wiki   │ │  File  │
│ Search │ │ Search │ │ Loader │
│  🔍   │ │  📖   │ │  📄   │
└───┬────┘ └───┬────┘ └───┬────┘
    └──────────┴──────────┘
                │
                ▼
┌───────────────────────┐
│   LLaMA 3.3 70B       │ ── Response generate
│   (via Groq)          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Streamlit UI        │ ── Streaming output
│   Chat Interface      │ ── History + Export
└───────────────────────┘
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 Web Search | DuckDuckGo দিয়ে real-time internet search |
| 📖 Wikipedia Search | যেকোনো বিষয়ে Wikipedia থেকে বিস্তারিত তথ্য |
| 📄 File Analysis | PDF ও TXT file upload করে analyze করা |
| 🌐 Multi-language | Bengali 🇧🇩 ও English 🇬🇧 response support |
| ⚡ Streaming Output | Real-time টাইপিং effect এ response |
| 💾 Chat History | Conversation save ও load করার সুবিধা |
| 📥 PDF Export | পুরো chat PDF এ export করা |
| 📋 Copy Button | যেকোনো response এক click এ copy |
| 🧠 ReAct Agent | Intelligent tool selection ও decision making |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Agent | LangGraph (ReAct) |
| LLM | LLaMA 3.3 70B via Groq |
| Tools | DuckDuckGo + Wikipedia |
| Framework | LangChain |
| Language | Python 3.10+ |
| Deployment | Hugging Face Spaces |

---

## 📁 Project Structure
```
Autonomous Research Agent/
│
├── 📄 app.py               # Streamlit UI & main application
├── 🤖 agent.py             # LangGraph ReAct agent setup
├── 🔧 tools.py             # Custom LangChain tools
├── 📋 requirements.txt     # Python dependencies
├── 🔒 .env                 # API keys (local only)
├── 🚫 .gitignore           # Git ignore rules
└── 📖 README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
```
Python 3.10+
Groq API Key → groq.com (Free)
```

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/mdmahabubalambishas/Autonomous Research Agent.git
cd Autonomous Research Agent
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

`.env` file বানাও project root এ —
```env
GROQ_API_KEY=your_groq_api_key_here
```

**5. Run the app**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🧪 Example Queries

### 🔍 Web Search
```
"LangGraph কী এবং কীভাবে কাজ করে?"
"২০২৫ সালে AI এর নতুন developments কী?"
"Latest news about OpenAI?"
```

### 📖 Wikipedia Research
```
"Artificial Intelligence এর ইতিহাস বিস্তারিত বলো"
"Quantum Computing কীভাবে কাজ করে?"
"Machine Learning vs Deep Learning পার্থক্য?"
```

### 📄 Document Analysis
```
১. Sidebar এ PDF upload করো
২. "এই document এর মূল বিষয় কী?" — জিজ্ঞেস করো
৩. "Summarize this document in Bengali"
```

---

## 🔍 How ReAct Agent Works
```
Step 1 → Thought
         Agent query analyze করে
         কোন tool দরকার সেটা decide করে

Step 2 → Action
         সঠিক tool select করে
         Web Search / Wikipedia / File Loader

Step 3 → Observation
         Tool এর result দেখে
         Answer sufficient কিনা check করে

Step 4 → Final Answer
         LLaMA 3.3 70B দিয়ে response generate করে
         Bengali বা English এ stream করে দেয়
```

---

## ⚙️ Configuration

**Model পরিবর্তন** (`agent.py`) —
```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # LLM model
    temperature=0.2,                   # Creativity (0-1)
    max_tokens=4096                    # Response length
)
```

**Custom Tool যোগ করা** (`tools.py`) —
```python
@tool
def my_custom_tool(query: str) -> str:
    """Tool description."""
    # Your logic here
    return result

all_tools = [search_tool, wikipedia_search, my_custom_tool]
```

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| Web Search response time | ~2-3 seconds |
| Wikipedia response time | ~1-2 seconds |
| PDF analysis time | ~3-5 seconds |
| Languages supported | Bengali, English |
| Max file size | 10MB |
| LLM model | LLaMA 3.3 70B |

---

## 💡 What I Learned
```
✅ LangGraph ReAct Agent
   Multi-step reasoning
   Intelligent tool selection
   State management

✅ Tool Integration
   DuckDuckGo web search
   Wikipedia API
   PDF/TXT file processing

✅ Streaming Response
   Real-time output
   Typing effect implementation

✅ Multilingual LLM
   Bengali language support
   Language detection
   Response formatting

✅ Chat Management
   Conversation history
   PDF export
   Copy functionality
```


## 🤝 Contributing
```bash
# Fork করো → Clone করো → Branch তৈরি করো
git checkout -b feature/AmazingFeature

# Changes করো → Commit করো
git commit -m "Add AmazingFeature"

# Push করো → Pull Request খোলো
git push origin feature/AmazingFeature
```

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

<div align="center">

**Md Mahabub Alam Bishal**
*AI/ML Engineer | LLM & Generative AI Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/md-mahabub-alam-bishal/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/mdmahabubalambishal)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Follow-FFD21E?style=for-the-badge)](https://huggingface.co/mahabub-unlocked)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:mdmahabubalambishal@gmail.com)

</div>

## 🙏 Acknowledgements

- [LangChain](https://langchain.com/) — LLM framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) — Agent orchestration
- [Groq](https://groq.com/) — Fast LLM inference
- [DuckDuckGo](https://duckduckgo.com/) — Privacy-first web search
- [Wikipedia](https://wikipedia.org/) — Knowledge base
- [Streamlit](https://streamlit.io/) — UI framework
- [Hugging Face](https://huggingface.co/) — Deployment platform

---

<div align="center">

⭐ **এই project টা useful লাগলে GitHub এ Star দাও!**

*Made with ❤️ by Mahabub*

**Live Demo:** [huggingface.co/spaces/mahabub-unlocked/QueryMind-AI](https://huggingface.co/spaces/mahabub-unlocked/QueryMind-AI)  
**GitHub:** [github.com/mdmahabubalambishal/QueryMind-AI](https://github.com/mdmahabubalambishal/Autonomous Research Agent)

</div>
