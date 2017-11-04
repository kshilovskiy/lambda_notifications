from tests.helpers import load_json
from functions.basic.notifier import notify
from unittest.mock import Mock, patch, ANY
import pytest

URL = 'http://myservice.com'
S3_PATH = 's3://sourcebucket/results.json'
EXPECTED_BODY = { 's3_path': S3_PATH }
EXPECTED_AUTH = ('user','pass')

CONSUMER = {
    'url': URL,
    'username': 'user',
    'password': 'pass'
}
#This will prevent any real requests
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@patch('functions.basic.notifier.requests.post')
def test_notification_is_sent(mock_post):
    notify(CONSUMER, S3_PATH)

    mock_post.assert_called_with(URL, json=EXPECTED_BODY, auth=EXPECTED_AUTH)
