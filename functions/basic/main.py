import os
import notifier
import event_parser

def handle(s3_event, context):
    receiver = _get_receiver()

    for event in s3_event['Records']:
        s3_path = event_parser.extract_s3_path(event)
        notifier.notify(receiver, s3_path)

def _get_receiver():
    return {
        'url': os.getenv('RECEIVER_URL'),
        'username': os.getenv('RECEIVER_USERNAME'),
        'password': os.getenv('RECEIVER_PASSWORD')
    }
