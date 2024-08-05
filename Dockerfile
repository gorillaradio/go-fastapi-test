# Usa l'immagine base di Python
FROM python:3.9-slim

# Installa i locali
RUN apt-get update && apt-get install -y locales && \
    sed -i -e 's/# it_IT.UTF-8 UTF-8/it_IT.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file delle dipendenze e installale
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto della directory corrente nella directory di lavoro del container
COPY . /app

# Espone la porta dell'applicazione
EXPOSE 8000

# Comando per avviare l'applicazione
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]