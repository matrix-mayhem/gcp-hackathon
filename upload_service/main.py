from fastapi import FastAPI, UploadFile
import logging
import os
import uvicorn
from google.cloud import pubsub_v1
import json
import uuid

app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("project-4438a580-ac32-4cf8-81c", "file-processing-topic")

@app.get("/")
def health():
    logger.info("Upload service running")
    return {"status": "upload service running"}


@app.post("/upload")
async def upload_file(file: UploadFile):
    file_id = str(uuid.uuid4())

    logger.info(f"Received file: {file.filename}")

    # Publish event
    publisher.publish(
        topic_path,
        json.dumps({"file_id": file_id}).encode()
    )

    logger.info(f"Message sent for file_id: {file_id}")

    return {"file_id": file_id}


#IMPORTANT: start server (same as worker)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

# from fastapi import FastAPI
# import os
# import uvicorn

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"status": "running"}

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     uvicorn.run(app, host="0.0.0.0", port=port)