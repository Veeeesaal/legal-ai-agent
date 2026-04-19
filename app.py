import streamlit as st
from crew.crew_setup import run_crew
import time

# Page config
st.set_page_config(page_title="Legal AI Assistant", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    .chat-user {
        background-color: #1E90FF;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 8px;
    }
    .chat-ai {
        background-color: #262730;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("⚖️ Legal AI Assistant")
st.caption("🚀 Agentic AI powered legal assistant")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("💡 Ask about IPC, laws, cases")
    st.write("⚡ CrewAI + Groq + Vector DB")
    st.sidebar.write("Built by Vishal 🚀")

# Chat history init
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-ai">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# Input
user_input = st.chat_input("Ask your legal question...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show user message
    st.markdown(f'<div class="chat-user">🧑 {user_input}</div>', unsafe_allow_html=True)

    # Get AI response
    with st.spinner("🤖 Thinking..."):
        response = run_crew(user_input)

    # 🔥 FIX: ensure response is string
    if isinstance(response, tuple):
        response = response[0]
    response = str(response)

    # Typing effect
    placeholder = st.empty()
    full_text = ""

    for char in response:
        full_text += char
        placeholder.markdown(
            f'<div class="chat-ai">🤖 {full_text}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.003)  # smoother speed

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response})