from google.cloud import storage


def list_buckets():

    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print(buckets)