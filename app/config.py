from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID", "").strip()
REGION = os.getenv("REGION", "").strip()

IAM_ACCOUNT = os.getenv("IAM_ACCOUNT", "").strip()

# O .strip() remove qualquer \r, \n ou espaço invisível!
BQ_DATASET = os.getenv("BQ_DATASET", "").strip()
BQ_TABLE = os.getenv("BQ_TABLE", "").strip()
BUCKET_NAME = os.getenv("BUCKET_NAME", "").strip()

MODELO_CHAT = os.getenv("MODELO_CHAT", "").strip()
MODELO_EMBEDDINGS = os.getenv("MODELO_EMBEDDINGS", "").strip()

TOP_K = int(os.getenv("TOP_K", "8"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "1024"))