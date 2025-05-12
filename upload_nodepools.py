from google.cloud import storage


def upload_to_gcs(
    bucket_name, source_file_path, destination_blob_name, credentials_file
):
    """Uploads a file to Google Cloud Storage."""

    storage_client = storage.Client.from_service_account_json(credentials_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)

    print(f"File {source_file_path} uploaded to {destination_blob_name}.")


if __name__ == "__main__":
    bucket_name = "model-service-deployment-resources"
    source_file_path = f"node_pools/node_pools.json"
    destination_blob_name = "node_pools.json"
    credentials_file = "creds.json"

    upload_to_gcs(
        bucket_name, source_file_path, destination_blob_name, credentials_file
    )
