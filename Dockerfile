FROM python:3.10-slim

# Install system dependencies and alignment tools
RUN apt-get update && \
    apt-get install -y \
      ncbi-blast+ \
      muscle \
      mafft \
      clustalo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["streamlit", "run", "app.py"]
