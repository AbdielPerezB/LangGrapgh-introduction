from dotenv import load_dotenv
import os, json
from google.oauth2 import service_account

load_dotenv()

#api keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

#llm's
MODEL_GEMINI = "gemini-1.5-flash"

#VertexAI
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_REGION = os.getenv("GCP_REGION")
GCP_CREDENTIALS_JSON = os.environ.get("GCP_CREDENTIALS_JSON")
credentials= service_account.Credentials.from_service_account_info(json.loads(GCP_CREDENTIALS_JSON))
scoped_creds = credentials.with_scopes(["https://www.googleapis.com/auth/cloud-platform"])
