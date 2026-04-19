import streamlit as st
from crew.crew_setup import run_crew
import time

st.set_page_config(
    page_title="LexAI — Legal Intelligence",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Root Reset ──────────────────────────────────── */
html, body, [class*="css"], .stApp {
    background-color: #080A0F !important;
    color: #E8E0CC !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Animated grid background ────────────────────── */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(197,161,83,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(197,161,83,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ─────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: #0C0F18 !important;
    border-right: 1px solid rgba(197,161,83,0.2) !important;
}

section[data-testid="stSidebar"] * {
    color: #E8E0CC !important;
}

/* sidebar header */
.sidebar-brand {
    padding: 2rem 0 1.5rem;
    text-align: center;
}
.sidebar-brand .brand-icon {
    font-size: 40px;
    display: block;
    margin-bottom: 8px;
    filter: drop-shadow(0 0 12px rgba(197,161,83,0.6));
}
.sidebar-brand h2 {
    font-family: 'Playfair Display', serif !important;
    font-size: 22px;
    font-weight: 700;
    color: #C5A153 !important;
    margin: 0;
    letter-spacing: 1px;
}
.sidebar-brand p {
    font-size: 11px;
    color: rgba(197,161,83,0.5) !important;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 4px 0 0;
}

.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(197,161,83,0.15);
    margin: 1rem 0;
}

.sidebar-section-label {
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(197,161,83,0.4) !important;
    margin: 0 0 8px;
    padding: 0;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(197,161,83,0.08);
    border: 1px solid rgba(197,161,83,0.2);
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 12px;
    color: #C5A153 !important;
    margin-bottom: 6px;
    width: 100%;
}
.status-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #4CAF72;
    box-shadow: 0 0 6px #4CAF72;
    flex-shrink: 0;
}

/* ── Stremlit Button Override ─────────────────────── */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(197,161,83,0.35) !important;
    color: #C5A153 !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    letter-spacing: 0.5px;
    padding: 8px 16px !important;
    transition: all 0.2s ease !important;
    width: 100%;
}
.stButton > button:hover {
    background: rgba(197,161,83,0.12) !important;
    border-color: #C5A153 !important;
    color: #E8C97A !important;
}

/* ── Main content area ───────────────────────────── */
.main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important;
    max-width: 860px !important;
}

/* ── Page Header ─────────────────────────────────── */
.lex-header {
    text-align: center;
    padding: 2.5rem 0 2rem;
    position: relative;
}
.lex-header::after {
    content: '';
    display: block;
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #C5A153, transparent);
    margin: 1.2rem auto 0;
}
.lex-header h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 42px !important;
    font-weight: 900 !important;
    color: #C5A153 !important;
    letter-spacing: -0.5px;
    line-height: 1.1;
    margin: 0;
}
.lex-header .subtitle {
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(197,161,83,0.45);
    margin: 8px 0 0;
}

/* ── Chat Messages ───────────────────────────────── */
.msg-wrapper {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-bottom: 20px;
}

.msg-user {
    align-self: flex-end;
    background: linear-gradient(135deg, #1C1708, #221D0A);
    border: 1px solid rgba(197,161,83,0.35);
    border-radius: 14px 14px 3px 14px;
    padding: 12px 18px;
    max-width: 78%;
    font-size: 14px;
    line-height: 1.6;
    color: #E8E0CC;
    position: relative;
}
.msg-user-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #C5A153;
    text-align: right;
    margin-bottom: 4px;
    opacity: 0.7;
}

.msg-ai {
    align-self: flex-start;
    background: #0F1219;
    border: 1px solid rgba(255,255,255,0.07);
    border-left: 2px solid #C5A153;
    border-radius: 3px 14px 14px 14px;
    padding: 14px 18px;
    max-width: 88%;
    font-size: 14px;
    line-height: 1.75;
    color: #D4CCBA;
}
.msg-ai-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(197,161,83,0.5);
    margin-bottom: 6px;
}

/* ── Chat Input ──────────────────────────────────── */
.stChatInput {
    background: #0C0F18 !important;
    border-top: 1px solid rgba(197,161,83,0.15) !important;
}
.stChatInput textarea, .stChatInput input {
    background: #0F1219 !important;
    border: 1px solid rgba(197,161,83,0.25) !important;
    border-radius: 10px !important;
    color: #E8E0CC !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    caret-color: #C5A153 !important;
}
.stChatInput textarea:focus, .stChatInput input:focus {
    border-color: rgba(197,161,83,0.55) !important;
    box-shadow: 0 0 0 3px rgba(197,161,83,0.07) !important;
}

/* ── Spinner ─────────────────────────────────────── */
.stSpinner > div {
    border-top-color: #C5A153 !important;
}

/* ── Empty state ─────────────────────────────────── */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    opacity: 0.5;
}
.empty-state .glyph {
    font-size: 48px;
    display: block;
    margin-bottom: 12px;
    filter: grayscale(0.4);
}
.empty-state p {
    font-size: 13px;
    letter-spacing: 1px;
    color: rgba(197,161,83,0.5);
    text-transform: uppercase;
}

/* ── Suggestion chips ────────────────────────────── */
.chips-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-top: 1.5rem;
}
.chip {
    background: rgba(197,161,83,0.06);
    border: 1px solid rgba(197,161,83,0.2);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    color: rgba(197,161,83,0.65);
    cursor: pointer;
    transition: all 0.2s;
}
.chip:hover {
    background: rgba(197,161,83,0.14);
    color: #C5A153;
}

/* ── Scrollbar ───────────────────────────────────── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(197,161,83,0.2); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(197,161,83,0.4); }

/* ── Hide Streamlit default elements ─────────────── */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <span class="brand-icon">⚖️</span>
        <h2>LexAI</h2>
        <p>Legal Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-section-label">System Status</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="status-pill"><span class="status-dot"></span> CrewAI — Online</div>
    <div class="status-pill"><span class="status-dot"></span> Groq LLM — Active</div>
    <div class="status-pill"><span class="status-dot"></span> Vector DB — Ready</div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-section-label">Topics I Know</p>', unsafe_allow_html=True)

    topics = ["IPC Sections", "Constitutional Law", "Criminal Procedure", "Civil Cases", "FIR & Bail", "Property Law"]
    for t in topics:
        st.markdown(f'<div style="font-size:13px; color:rgba(197,161,83,0.6); padding:4px 0; border-bottom:1px solid rgba(197,161,83,0.06);">→ {t}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    if st.button("🧹  Clear Conversation"):
        st.session_state.messages = []
        st.rerun()


# ── Page Header ────────────────────────────────────────────
st.markdown("""
<div class="lex-header">
    <h1>Legal Intelligence</h1>
    <p class="subtitle">Agentic AI · Indian Law · IPC · Precedents</p>
</div>
""", unsafe_allow_html=True)


# ── Chat state ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []


# ── Empty state ────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <span class="glyph">⚖️</span>
        <p>Ask your legal question to begin</p>
    </div>
    <div class="chips-row">
        <span class="chip">IPC Section 302</span>
        <span class="chip">Bail kaise milti hai?</span>
        <span class="chip">Property dispute</span>
        <span class="chip">FIR file karna</span>
        <span class="chip">Consumer rights</span>
    </div>
    """, unsafe_allow_html=True)


# ── Render history ─────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="msg-wrapper">
            <div class="msg-user-label">You</div>
            <div class="msg-user">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="msg-wrapper">
            <div class="msg-ai-label">⚖ LexAI</div>
            <div class="msg-ai">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)


# ── Chat Input ─────────────────────────────────────────────
user_input = st.chat_input("Ask your legal question in Hindi or English…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"""
    <div class="msg-wrapper">
        <div class="msg-user-label">You</div>
        <div class="msg-user">{user_input}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Consulting legal database…"):
        response = run_crew(user_input)

    if isinstance(response, tuple):
        response = response[0]
    response = str(response)

    placeholder = st.empty()
    full_text = ""

    for char in response:
        full_text += char
        placeholder.markdown(f"""
        <div class="msg-wrapper">
            <div class="msg-ai-label">⚖ LexAI</div>
            <div class="msg-ai">{full_text}▌</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.003)

    placeholder.markdown(f"""
    <div class="msg-wrapper">
        <div class="msg-ai-label">⚖ LexAI</div>
        <div class="msg-ai">{response}</div>
    </div>
    """, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": response})