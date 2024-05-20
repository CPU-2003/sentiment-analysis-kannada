from transformers import pipeline
from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from deep_translator import GoogleTranslator
def model(text:str):
    translated_text = GoogleTranslator(source='kn', target='en').translate(text)
    return translated_text

def modell(word:str):
    translated_text = GoogleTranslator(source='en', target='kn').translate(word)
    return translated_text
  
app = FastAPI()

# Load sentiment analysis model
nlp = pipeline(task='sentiment-analysis',
               model='nlptown/bert-base-multilingual-uncased-sentiment')

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    probability: float
    sentiment: str

def analyze_sentiment(text):
    """Get and process result"""
    t_text = model(text)
    result = nlp(t_text)


    sentiment = ''
    if (result[0]['label'] == '1 star'):
        sentiment = 'very negative'
    elif (result[0]['label'] == '2 star'):
        sentiment = 'negative'
    elif (result[0]['label'] == '3 stars'):
        sentiment = 'neutral'
    elif (result[0]['label'] == '4 stars'):
        sentiment = 'positive'
    else:
        sentiment = 'very positive'

    probability = result[0]['score']

    # Format and return results
    return probability, sentiment
  
@app.get('/')
def send():
    return {"Message":"A sentiment analysis application"}

@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    probability, sentiment = analyze_sentiment(request.text)
    return SentimentResponse(
        probability=probability, sentiment=sentiment
    )