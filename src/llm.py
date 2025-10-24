# def get_llm():
#     try:
#         from langchain_google_vertexai import VertexAI
        
#         project_id = os.getenv("GCP_PROJECT_ID")
#         location = os.getenv("GCP_LOCATION", "us-central1")
        
#         if not project_id:
#             st.error("❌ GCP Project ID not found")
#             return None
            
#         st.success("✅ Initializing Vertex AI...")
#         return VertexAI(
#             project=project_id,
#             location=location,
#             model_name="gemini-pro"
#         )
#     except Exception as e:
#         st.error(f"❌ Vertex AI Error: {str(e)}")
#         return None
        