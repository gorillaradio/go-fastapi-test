from fastapi import FastAPI
from pydantic import BaseModel
from textproc import remove_stopwords, most_frequent_words, array_to_json

app = FastAPI()

class TextRequest(BaseModel):
    text: str
    n: int = 10

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/process-text")
def process_text(request: TextRequest):
    cleaned_text = remove_stopwords(request.text)
    frequent_words = most_frequent_words(cleaned_text, request.n)
    result_json = array_to_json(frequent_words)
    return {"result": result_json}