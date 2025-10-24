from langchain_core.prompts import PromptTemplate
from src.llm import get_llm
import streamlit as st

st.set_page_config("Simple Chat Bot", page_icon="🧠", layout="wide")

# Add modern CSS styling
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
    }
    
    /* Title styling */
    h1 {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
    }
    
    /* Input field styling */
    .stTextInput>div>div>input {
        border-radius: 25px;
        border: 2px solid #667eea;
        padding: 12px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 2px rgba(118, 75, 162, 0.2);
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    /* Bot response styling */
    .stMarkdown {
        background: black;
        padding: 15px 20px;
        border-radius: 15px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
    }
    
    /* Warning message styling */
    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

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