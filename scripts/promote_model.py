import os
import mlflow

def promote_model():
    # Set up DagsHub credentials for MLflow tracking
    # Updated to look for the variable we defined in ci.yaml
    dagshub_token = os.getenv("DAGSHUB_USER_TOKEN")
    if not dagshub_token:
        raise EnvironmentError("DAGSHUB_USER_TOKEN environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "hemantjangidn-blip"
    repo_name = "Capstone-Project"

    # Set up MLflow tracking URI
    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

    client = mlflow.MlflowClient()

    model_name = "my_model"
    
    # 1. Safely check if a model exists in Staging
    staging_versions = client.get_latest_versions(model_name, stages=["Staging"])
    if not staging_versions:
        print(f"No model found in 'Staging' stage for '{model_name}'.")
        print("Note: Ensure your training/evaluation script transitions the registered model to 'Staging'. Exiting gracefully.")
        return 
        
    latest_version_staging = staging_versions[0].version

    # 2. Safely check if a model exists in Production before archiving
    prod_versions = client.get_latest_versions(model_name, stages=["Production"])
    if prod_versions:
        for version in prod_versions:
            client.transition_model_version_stage(
                name=model_name,
                version=version.version,
                stage="Archived"
            )
            print(f"Archived previous production version: {version.version}")

    # Promote the new model to production
    client.transition_model_version_stage(
        name=model_name,
        version=latest_version_staging,
        stage="Production"
    )
    print(f"Model version {latest_version_staging} successfully promoted to Production")

if __name__ == "__main__":
    promote_model()