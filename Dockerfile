# Usa l'immagine base di Python
FROM python:3.9-slim

# Installa i locali italiani
RUN apt-get update && apt-get install -y locales && \
    echo "it_IT.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=it_IT.UTF-8

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file delle dipendenze e installale
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto della directory corrente nella directory di lavoro del container
COPY . /app

# Espone la porta dell'applicazione
EXPOSE 8000

# Imposta il locale
ENV LANG=it_IT.UTF-8
ENV LANGUAGE=it_IT:it
ENV LC_ALL=it_IT.UTF-8

# Comando per avviare l'applicazione
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]