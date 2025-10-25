from dotenv import load_dotenv
import os

# --- Load environment variables ---
load_dotenv()

def get_llm():
    try:
        from langchain_google_vertexai import VertexAI

        project_id = os.getenv("GCP_PROJECT_ID")
        location = os.getenv("GCP_LOCATION", "us-central1")

        if not project_id:

            return None

        return VertexAI(
            project=project_id,
            location=location,
            model_name="gemini-2.5-flash"
        )
    except Exception as e:
        return None