# deel-home-work
      gcloud iam service-accounts add-iam-policy-binding "github-actions@deel-home-task-1.iam.gserviceaccount.com" \
          --project="deel-home-task-1" \
          --role="roles/iam.workloadIdentityUser" \
          --member="principalSet://iam.googleapis.com/projects/499613830332/locations/global/workloadIdentityPools/deel/attribute.repository/eladtamari/deel-home-work"

          gcloud iam service-accounts add-iam-policy-binding "github-actions-sa@deel-home-task-1.iam.gserviceaccount.com" \
          --project="deel-home-task-1" \
          --role="roles/iam.serviceAccountTokenCreator" \
          --member="principalSet://iam.googleapis.com/projects/499613830332/locations/global/workloadIdentityPools/deel/attribute.repository/eladtamari/deel-home-work"

          gcloud iam service-accounts add-iam-policy-binding "github-actions-sa@<YOUR_PROJECT_ID>.iam.gserviceaccount.com" \
          --role="roles/iam.serviceAccountTokenCreator" \
          --member="principalSet://iam.googleapis.com/projects/<YOUR_PROJECT_NUMBER>/locations/global/workloadIdentityPools/github-actions-pool/attribute.repository/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>"




steps:
- id: auth
  uses: google-github-actions/auth@v0.4.0
  with:
    workload_identity_provider: 'projects/123456789/locations/global/workloadIdentityPools/my-pool/providers/my-provider'
    service_account: 'my-service-account@my-project.iam.gserviceaccount.com'

- id: get-gke-credentials
  uses: google-github-actions/get-gke-credentials@v0.4.0
  with:
    cluster_name: my-cluster
    location: us-central1-a

- id: get-pods
  run: kubectl get pods


  steps:
- id: 'auth'
  name: 'Authenticate to Google Cloud'
  uses: 'google-github-actions/auth@v0.4.0'
  with:
    token_format: 'access_token'
    workload_identity_provider: 'projects/123456789/locations/global/workloadIdentityPools/my-pool/providers/my-provider'
    service_account: 'my-service-account@my-project.iam.gserviceaccount.com'

- name: 'Access secret'
  run: |-
    curl https://secretmanager.googleapis.com/v1/projects/499613830332/secrets/my-secret/versions/1:access \
      --header "Authorization: Bearer ${{ steps.auth.outputs.access_token }}"