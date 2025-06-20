FROM python:3.10-slim

RUN apt-get update && apt-get install -y ncbi-blast+ muscle mafft clustalo && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
