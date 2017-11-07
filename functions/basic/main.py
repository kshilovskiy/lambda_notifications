import os
import logging
import notifier
import event_parser

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(s3_event, context):
    consumer = _get_consumer()

    for event in s3_event['Records']:
        s3_path = event_parser.extract_s3_path(event)
        logger.info(f"Extracted path {s3_path}")

        notifier.notify(consumer, s3_path)

def _get_consumer():
    return {
        'url': os.getenv('CONSUMER_URL'),
        'username': os.getenv('CONSUMER_USERNAME'),
        'password': os.getenv('CONSUMER_PASSWORD')
    }
