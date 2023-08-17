
import json
from google.cloud import storage, bigquery

storage_client = storage.Client()
bq_client = bigquery.Client()

def read_from_gcs(bucket_name, blob_name):

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)


    with blob.open("r") as f:
        data_str = f.read()

    out = json.loads(data_str)

    return out

def write_to_bq(data,table):
    rows_to_insert = [data]

    errors = bq_client.insert_rows_json(table, rows_to_insert)  
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
        
def delete_blob(bucket_name, blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    generation_match_precondition = None

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to delete is aborted if the object's
    # generation number does not match your precondition.
    blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
    generation_match_precondition = blob.generation

    blob.delete(if_generation_match=generation_match_precondition)

    print(f"Blob {blob_name} deleted.")