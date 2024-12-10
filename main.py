from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# modelo pré-treinado Sentiment Analysis
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
    allow_origins=["*"],  # "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)
