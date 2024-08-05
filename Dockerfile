# Usa l'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file delle dipendenze e installale
COPY requirements.lock /app/requirements.lock
RUN pip install -r requirements.lock

# Copia tutto il contenuto della directory corrente nella directory di lavoro del container
COPY . /app

# Comando per avviare l'applicazione
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]