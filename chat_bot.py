from langchain_core.prompts import PromptTemplate
from src.llm import get_llm
import streamlit as st



# --- Streamlit page setup ---
st.set_page_config("Simple Chat Bot", page_icon="🧠", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Global background and font */
    body {
        background-color: #0e1117;
        color: #fafafa;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title styling */
    h1 {
        text-align: center;
        color: #00b4d8;
        text-shadow: 1px 1px 2px #000;
        margin-bottom: 30px;
    }

    /* Input box styling */
    div[data-baseweb="input"] > div {
        background-color: #1e1e2f !important;
        color: #fff !important;
        border-radius: 10px !important;
        border: 1px solid #3a3a4f !important;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #00b4d8;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #0077b6;
        transform: scale(1.05);
    }

    /* Chat message box */
    .chat-box {
        background-color: #1e1e2f;
        border-radius: 10px;
        padding: 1rem;
        margin-top: 1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    /* Bot text */
    .bot-response {
        color: #90e0ef;
        font-weight: 500;
    }

    /* Warning style override */
    .stAlert {
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🧠 Simple Chat Bot")

# --- LLM Initialization ---


# --- Initialize the model ---
llm = get_llm()

# --- Define Prompt Template ---
template = """You are a helpful chatbot.
Answer the user's question clearly.

Question: {user_question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["user_question"],
    template=template
)

# --- Create chain ---
if llm:
    chain = prompt | llm
else:
    chain = None

# --- Input field ---
user_input = st.text_input("💬 Enter your question:")

# --- Button click event ---
if st.button("Send"):
    if user_input:
        if user_input.lower() in ["exit", "quit", "bye"]:
            st.markdown('<div class="chat-box"><span class="bot-response">**Bot:** Goodbye 👋</span></div>', unsafe_allow_html=True)
        else:
            if chain:
                answer = chain.invoke({"user_question": user_input})
                st.markdown(f'<div class="chat-box"><span class="bot-response">Bot: {answer}</span></div>', unsafe_allow_html=True)
            else:
                st.error("Model not initialized. Please check your Vertex AI configuration.")
    else:
        st.warning("Please enter a question!")
