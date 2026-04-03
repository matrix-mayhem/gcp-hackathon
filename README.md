# gcp-hackathon
gcloud init
# You are Owner or Editor of project
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

gcloud services enable run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  pubsub.googleapis.com \
  firestore.googleapis.com

gcloud projects describe YOUR_PROJECT_ID --format="value(projectNumber)"

# Setting roles for storage and codebuild
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member=serviceAccount:123456789@cloudbuild.gserviceaccount.com \
  --role=roles/storage.objectAdmin

Cloud Build Service Account
        ↓ (now allowed)
Cloud Storage Bucket
        ↓
Upload + Read build files

# Settting roles for Compute
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member=serviceAccount:939090702834-compute@developer.gserviceaccount.com \
  --role=roles/storage.objectAdmin

Compute Service Account
        ↓ (now allowed)
Cloud Storage (build staging bucket)
        ↓
Build succeeds

# create repository in artifact registry
gcloud artifacts repositories create my-repo --repository-format=docker --location=asia-south1

# serverless version of docker build and docker push that happens entirely in the cloud.
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/app
gcloud builds submit --tag asia-south1-docker.pkg.dev/project-4438a580-ac32-4cf8-81c/my-repo/app ./upload_serive


# Backend is alive
gcloud run deploy app \
  --image asia-south1-docker.pkg.dev/YOUR_PROJECT_ID/app \
  --platform managed \
  --allow-unauthenticated

# Latest Logs
gcloud run services logs read upload-service \
  --region asia-south1 \
  --limit 50

# Deployed services
gcloud run services list
gcloud artifacts repositories list
gcloud compute instances list
gcloud compute instances stop INSTANCE_NAME
gcloud sql instances list
gcloud redis instances list
gcloud container clusters list
gcloud container clusters list
gcloud run services describe SERVICE_NAME


# Deleting services
gcloud run services delete SERVICE_NAME --region REGION

# PubSub
gcloud pubsub topics create file-processing-topic

# Provides URL
gcloud run services describe worker-service --region asia-south1 --format="value(status.url)"
https://worker-service-37lu5a63oq-el.a.run.app

gcloud pubsub subscriptions create file-sub --topic file-processing-topic --push-endpoint=https://worker-service-37lu5a63oq-el.a.run.app --push-auth-service-account=939090702834-compute@developer.gserviceaccount.com

# GCP Microservices Project

## Services
- Gateway (JWT auth)
- Upload Service
- Worker Service

## Flow
Upload → Pub/Sub → Worker → Firestore

## Stack
Cloud Run, Pub/Sub, Firestore, Cloud Storage, Cloud Build