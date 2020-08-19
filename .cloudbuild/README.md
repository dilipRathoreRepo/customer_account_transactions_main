# Customer-Account-Transactions Cloud Build CI/CD

Customer-Account-Transactions is a Python library for processing and analyzing customer's transactions records and generate meaning ful insights.

## Cloud Build Process (build.cloudbuild.yaml)

1. Build Kubernetes POD image.

## Cloud Build Process (deploy.cloudbuild.yaml)

1. Get Kubernetes credentials - Uses gcloud get credentials command to fetch kubernetes cluster's credentials
2. Delete the Kubernetes POD once the task is completed
