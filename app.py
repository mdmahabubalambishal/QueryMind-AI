import streamlit as st
import json
import os
import time
from datetime import datetime
from agent import create_agent

# ── Page Config ─────────────────────────────────────
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ───────────────────────────────────────
st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(90deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    .stChatInput > div {
        border-radius: 15px !important;
        border: 2px solid #667eea !important;
    }
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        color: #667eea;
        padding: 10px 0 0 0;
        margin: 0;
    }
    .main-subtitle {
        text-align: center;
        color: #888;
        font-size: 0.95rem;
        margin-top: 4px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ── Main Header ──────────────────────────────────────
st.markdown('<p class="main-title">🤖 AI Research Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Powered by LangGraph • Groq • LLaMA 3.3 70B</p>', unsafe_allow_html=True)

# ── Session State ───────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "language" not in st.session_state:
    st.session_state.language = "bengali"
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = ""

# ── Helper: Save/Load History ────────────────────────
HISTORY_FILE = "chat_history.json"

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)
    st.success("✅ Saved!")

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            st.session_state.messages = json.load(f)
        st.success("✅ Loaded!")
    else:
        st.warning("No history found.")

# ── Helper: PDF Export ───────────────────────────────
def export_pdf():
    try:
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        pdf.cell(200, 10, "AI Research Assistant - Chat Export", ln=True, align="C")
        pdf.cell(200, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align="C")
        pdf.ln(5)
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "Assistant"
            pdf.set_font("Helvetica", style="B", size=11)
            pdf.cell(200, 8, f"{role}:", ln=True)
            pdf.set_font("Helvetica", size=10)
            content = msg["content"].encode("latin-1", errors="replace").decode("latin-1")
            pdf.multi_cell(0, 7, content)
            pdf.ln(3)
        pdf_path = "chat_export.pdf"
        pdf.output(pdf_path)
        return pdf_path
    except Exception as e:
        st.error(f"PDF error: {e}")
        return None

# ── Helper: Extract PDF Text ─────────────────────────
def extract_pdf_text(uploaded_file):
    try:
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(uploaded_file.read()))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text[:3000]
    except Exception as e:
        return f"PDF read error: {e}"

# ── Sidebar ──────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # Language Toggle
    st.markdown("### 🌐 Language")
    lang = st.radio(
        "Response Language:",
        ["Bengali 🇧🇩", "English 🇬🇧"],
        index=0 if st.session_state.language == "bengali" else 1,
        horizontal=True
    )
    st.session_state.language = "bengali" if "Bengali" in lang else "english"

    st.divider()

    # File Upload
    st.markdown("### 📁 File Upload")
    uploaded_file = st.file_uploader(
        "PDF বা Text file upload করো",
        type=["pdf", "txt"]
    )
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            st.session_state.pdf_content = extract_pdf_text(uploaded_file)
        else:
            st.session_state.pdf_content = uploaded_file.read().decode("utf-8")[:3000]
        st.success(f"✅ File loaded! ({len(st.session_state.pdf_content)} chars)")
        st.info("এখন file সম্পর্কে প্রশ্ন করো!")

    if st.session_state.pdf_content:
        if st.button("🗑️ Remove File"):
            st.session_state.pdf_content = ""
            st.rerun()

    st.divider()

    # Tools Info
    st.markdown("### 🛠️ Tools")
    st.markdown("""
    - 🔍 **Web Search**
    - 📖 **Wikipedia**
    - 📄 **File Analyze**
    """)

    st.divider()

    # Chat History
    st.markdown("### 💾 History")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save"):
            save_history()
    with col2:
        if st.button("📂 Load"):
            load_history()
            st.rerun()

    st.divider()

    # PDF Export
    st.markdown("### 📄 Export")
    if st.button("📥 Export PDF"):
        path = export_pdf()
        if path:
            with open(path, "rb") as f:
                st.download_button(
                    label="⬇️ Download",
                    data=f,
                    file_name="chat_export.pdf",
                    mime="application/pdf"
                )

    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by LangGraph + Groq ⚡")

# ── File context indicator ───────────────────────────
if st.session_state.pdf_content:
    st.info("📄 File uploaded — এই file সম্পর্কে প্রশ্ন করতে পারো!")

st.divider()

# ── Chat Messages ────────────────────────────────────
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant":
            if st.button(f"📋 Copy", key=f"copy_{i}"):
                st.code(msg["content"])

# ── Chat Input ───────────────────────────────────────
placeholder = "প্রশ্ন করুন..." if st.session_state.language == "bengali" else "Ask a question..."
user_input = st.chat_input(placeholder)

if user_input:
    full_input = user_input
    if st.session_state.pdf_content:
        full_input = f"""User question: {user_input}

Relevant document content:
{st.session_state.pdf_content}

Please answer the question based on the document content above."""

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("⏳ Thinking..."):
            try:
                agent_executor = create_agent(st.session_state.language)

                with st.expander("🔧 Agent Process", expanded=False):
                    result = agent_executor.invoke({
                        "messages": [("human", full_input)]
                    })
                    for msg in result["messages"]:
                        msg_type = type(msg).__name__
                        if msg_type == "AIMessage":
                            if hasattr(msg, "tool_calls") and msg.tool_calls:
                                for tc in msg.tool_calls:
                                    st.info(f"🔧 **Tool:** `{tc['name']}`")
                        elif msg_type == "ToolMessage":
                            st.success(f"📦 **Result:** {msg.content[:200]}...")

                full_response = result["messages"][-1].content

                # Streaming effect
                displayed = ""
                for char in full_response:
                    displayed += char
                    message_placeholder.markdown(displayed + "▌")
                    time.sleep(0.008)

                message_placeholder.markdown(full_response)

                if st.button("📋 Copy Response", key="copy_new"):
                    st.code(full_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })

            except Exception as e:
                st.error(f"❌ Error: {e}")