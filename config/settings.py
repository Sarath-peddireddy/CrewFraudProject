import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME = 'gpt-3.5-turbo'
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

settings = Settings()