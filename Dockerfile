FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN mkdir -p /data && chmod 777 /data

VOLUME [ "/data" ]

EXPOSE 5000

CMD ["python", "main.py"]  


