from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Carregue um modelo pré-treinado (Exemplo: Sentiment Analysis)
sentiment_analysis = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(input: TextInput):
    result = sentiment_analysis(input.text)
    return {"analysis": result}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sentiment Analysis API. Use /docs for API documentation."}

@app.get("/favicon.ico")
async def get_favicon():
    return {"message": "Favicon not found"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou use ["http://localhost:3000"] para restringir ao front-end
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP, incluindo OPTIONS
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
