# Usa l'immagine base di Python
FROM python:3.9-slim

# Installa le localizzazioni e altre dipendenze necessarie
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/*

# Configura la locale
RUN sed -i '/it_IT.UTF-8/s/^# //g' /etc/locale.gen && locale-gen

# Imposta le variabili di ambiente per la locale
ENV LANG it_IT.UTF-8
ENV LANGUAGE it_IT:it
ENV LC_ALL it_IT.UTF-8

# Imposta la directory di lavoro
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