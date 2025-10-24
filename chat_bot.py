from langchain_core.prompts import PromptTemplate
from src.llm import get_llm
import streamlit as st
import os

st.set_page_config("Simple Chat Bot", page_icon="🧠", layout="wide")

def get_llm():
    try:
        from langchain_google_vertexai import VertexAI
        
        project_id = os.getenv("GCP_PROJECT_ID")
        location = os.getenv("GCP_LOCATION", "us-central1")
        
        if not project_id:
            st.error("❌ GCP Project ID not found")
            return None
            
        st.success("✅ Initializing Vertex AI...")
        return VertexAI(
            project=project_id,
            location=location,
            model_name="gemini-pro"
        )
    except Exception as e:
        st.error(f"❌ Vertex AI Error: {str(e)}")
        return None


st.title("🧠 Simple Chat Bot")

# Initialize the model
llm = get_llm()

# Define a prompt template
template = """You are a helpful chatbot.
Answer the user's question clearly.

Question: {user_question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["user_question"],
    template=template
)

# Create a chain (LangChain Expression Language style)
chain = prompt | llm

# Input field
user_input = st.text_input("Enter your question:")

# Button click event
if st.button("Send"):
    if user_input:
        if user_input.lower() in ["exit", "quit", "bye"]:
            st.write("**Bot:** Goodbye 👋")
        else:
            
            answer = chain.invoke({"user_question": user_input})
            # Display answer
            st.write("**Bot:**", answer.content if hasattr(answer, "content") else answer)
    else:
        st.warning("Please enter a question!")