FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn google-cloud-firestore google-cloud-storage

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]