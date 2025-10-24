from langchain_google_vertexai import VertexAI
import os

project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION", "us-central1")
        

def get_llm(model="gemini-2.5-flash-lite"):

    return VertexAI(
            project=project_id,
            location=location,
            model_name=model,
            max_output_tokens=256,
            temperature=0.1
        )