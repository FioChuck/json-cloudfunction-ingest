import requests
import os
from google.cloud import pubsub_v1
import json


def fetch_message():

    url = "https://data.alpaca.markets/v2/stocks/GOOGL/snapshot"

    # https://data.alpaca.markets/v2/stocks/GOOGL/trades/latest
    # https://data.alpaca.markets/v2/stocks/GOOGL/snapshot

    key_id = os.getenv('KEY_ID')
    secret_key = os.getenv('SECRET_KEY')

    payload = {}
    headers = {
        'Apca-Api-Key-Id': key_id,
        'Apca-Api-Secret-Key': secret_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    out = response.json()

    return out


def publish_message(data):
    project_id = os.getenv('PROJECT_ID')
    topic_id = os.getenv('TOPIC_ID')

    publisher = pubsub_v1.PublisherClient()  # instantiate client

    topic_path = publisher.topic_path(project_id, topic_id)

    message_json = json.dumps(data)
    message_bytes = message_json.encode('utf-8')

    future = publisher.publish(topic_path, message_bytes)
    print(future.result())

    return


def main(request):
    api_results = fetch_message()
    publish_message(api_results)

    return 'success'


# main('')
