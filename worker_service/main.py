from fastapi import FastAPI, Request
from google.cloud import firestore
import base64, json, logging
import os
import uvicorn

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = firestore.Client()


@app.get("/")
def health():
    return {"status": "worker running"}


@app.post("/")
async def process_message(request: Request):
    body = await request.json()

    message = body["message"]["data"]
    decoded = json.loads(base64.b64decode(message).decode())

    file_id = decoded.get("file_id", "unknown")

    logger.info(f"Processing file: {file_id}")

    db.collection("files").document(file_id).set({
        "status": "processed"
    })

    return {"status": "done"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)