# gcp-hackathon
gcloud init
# You are Owner or Editor of project
gcloud config set project YOUR_PROJECT_ID


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
gcloud builds submit --tag asia-south1-docker.pkg.dev/project-4438a580-ac32-4cf8-81c/my-repo/app


# Backend is alive
gcloud run deploy app \
  --image asia-south1-docker.pkg.dev/YOUR_PROJECT_ID/app \
  --platform managed \
  --allow-unauthenticated

