import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_vertexai import VertexAI

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="Gemini Chat Bot", page_icon="🤖", layout="wide")

# Inject basic CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
        }
        h1 {
            color: #333333;
        }
        .stTextInput > div > input {
            background-color: #ffffff;
            border: 1px solid #cccccc;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stSpinner {
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Gemini Chat Bot")

# Read environment variables
project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION", "us-central1")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Validate environment
missing_vars = []
if not project_id:
    missing_vars.append("GCP_PROJECT_ID")
if not credentials_path:
    missing_vars.append("GOOGLE_APPLICATION_CREDENTIALS")

if missing_vars:
    st.error(f"Missing environment variables: {', '.join(missing_vars)}")
    st.stop()

# Initialize Vertex AI
try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    llm = VertexAI(
        model="gemini-2.5-pro",
        project=project_id,
        location=location
    )
except Exception as e:
    st.error(f"Vertex AI connection failed:\n\n{e}")
    st.stop()

# Chat UI
st.subheader("💬 Ask me anything")
user_question = st.text_input("Your question:", placeholder="e.g. What is LangChain?")
submit = st.button("Ask")

if submit and user_question:
    with st.spinner("Thinking..."):
        try:
            response = llm.invoke(user_question)
            st.markdown("### Response")
            st.markdown(f"<div style='background-color:#ffffff;padding:15px;border-radius:5px;border:1px solid #ddd;'>{response}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Failed to get response:\n\n{e}")