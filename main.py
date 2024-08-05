from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configura il CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permette tutte le origini
    allow_credentials=True,
    allow_methods=["*"],  # Permette tutti i metodi
    allow_headers=["*"],  # Permette tutti gli headers
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/new-endpoint/{value}")
def new_endpoint(value: str):
    return {"message": f"You passed the value: {value}"}