from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")

IAM_ACCOUNT = os.getenv("IAM_ACCOUNT")

BQ_DATASET = os.getenv("BQ_DATASET")
BUCKET_NAME = os.getenv("BUCKET_NAME")
BQ_TABLE = os.getenv("BQ_TABLE")

MODELO_CHAT = os.getenv("MODELO_CHAT")
MODELO_EMBEDDINGS = os.getenv("MODELO_EMBEDDINGS")

TOP_K = int(os.getenv("TOP_K"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS"))