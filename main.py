import logging
import locale
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting application")

try:
    locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')
    logger.info("Locale set to it_IT.UTF-8")
except locale.Error as e:
    logger.error(f"Locale setting failed: {e}")

app = FastAPI()

# Configura il CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permette tutte le origini
    allow_credentials=True,
    allow_methods=["*"],  # Permette tutti i metodi
    allow_headers=["*"],  # Permette tutti gli headers
)

# Imposta la localizzazione italiana per i nomi dei mesi
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/formatdata/{data}")
def format_data(data: str):
    try:
        # Converte la stringa in un oggetto datetime
        data_obj = datetime.strptime(data, "%d-%m-%Y")
        
        # Formatta la data come richiesto
        mese = data_obj.strftime("%B")  # Nome completo del mese
        giorno = data_obj.strftime("%d")
        anno = data_obj.strftime("%Y")
        
        # Crea il testo di risposta
        risposta = f"La data che hai inserito è il giorno {giorno} {mese.capitalize()} dell'anno {anno}."
        
        return {"messaggio": risposta}
    except ValueError:
        # Se la data non è nel formato corretto, solleva un'eccezione
        raise HTTPException(status_code=400, detail="Formato data non valido. Usa DD-MM-YYYY.")