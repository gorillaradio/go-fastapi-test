from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Dizionario per i nomi dei mesi in italiano
mesi = {
    1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile",
    5: "maggio", 6: "giugno", 7: "luglio", 8: "agosto",
    9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre"
}

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
        # Converti la data in una stringa formattata manualmente
        giorno = date_obj.day
        mese = mesi[date_obj.month]
        anno = date_obj.year
        formatted_date = f"Oggi è il {giorno} {mese} {anno}"
        return {"message": formatted_date}
    except ValueError:
        return {"error": "Formato data non valido. Usa il formato dd-mm-yyyy."}

@app.get("/test-characters")
def test_characters():
    text = "Questa è una