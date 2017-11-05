import requests
import logging

logger = logging.getLogger()

def notify(receiver, s3_path):
    request = _build_request(receiver, s3_path)

    logger.info(f"Recepient: {request['url']}\nBody: {request['body']}")

    requests.post(request['url'], json=request['body'], auth=request['auth'])

def _build_request(receiver, s3_path):
    return {
        'url': receiver['url'],
        'auth': (receiver['username'], receiver['password']),
        'body': {'s3_path': s3_path}
    }
