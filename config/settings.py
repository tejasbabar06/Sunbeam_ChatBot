import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "scraper")
VECTOR_DB_PATH = os.path.join(BASE_DIR, "data", "knowledge_base")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


LLM_MODEL = "llama-3.3-70b-versatile"


