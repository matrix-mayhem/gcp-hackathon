from fastapi import FastAPI, UploadFile
from google.cloud import firestore, storage
import uuid

app = FastAPI()

db = firestore.Client()
storage_client = storage.Client()
bucket = storage_client.bucket("mybucket")

@app.post("/upload")
async def upload_file(file: UploadFile):
    file_id = str(uuid)

    blob = bucket.blob(file.filename)
    blob.upload_from_file(file.file)

    doc_ref = db.collection("files").document(file_id)
    doc_ref.set({
        "filename": file.filename,
        "status":"uploaded"}
    )

    return {"file_id": file_id}

@app.get("/files")
def get_files():
    docs = db.collection("files").strea()
    return [doc.to_dict for doc in docs]