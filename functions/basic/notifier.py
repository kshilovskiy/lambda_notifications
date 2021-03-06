import requests
import logging

logger = logging.getLogger()

def notify(consumer, s3_path):
    request = _build_request(consumer, s3_path)

    logger.info(f"Recepient: {request['url']}\nBody: {request['body']}")

    requests.post(request['url'], json=request['body'], auth=request['auth'])

def _build_request(consumer, s3_path):
    return {
        'url': consumer['url'],
        'auth': (consumer['username'], consumer['password']),
        'body': {'s3_path': s3_path}
    }
