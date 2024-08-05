# Usa l'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file delle dipendenze e installale
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Scarica le risorse necessarie di NLTK
RUN python -m nltk.downloader stopwords

# Copia tutto il contenuto della directory corrente nella directory di lavoro del container
COPY . /app

# Espone la porta dell'applicazione
EXPOSE 8000

# Comando per avviare l'applicazione
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]