from fastapi import FastAPI
from datetime import datetime
import locale

app = FastAPI()

# Imposta la localizzazione in italiano
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/new-endpoint/{value}")
def new_endpoint(value: str):
    return {"message": f"You passed the value: {value}"}

@app.get("/convert-date/{date_str}")
def convert_date(date_str: str):
    try:
        # Parla la data dal formato dd-mm-yyyy
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        # Converti la data in una stringa formattata
        formatted_date = date_obj.strftime("Oggi è il %d %B %Y")
        return {"message": formatted_date}
    except ValueError:
        return {"error": "Formato data non valido. Usa il formato dd-mm-yyyy."}