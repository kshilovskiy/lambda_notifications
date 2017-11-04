from tests.helpers import load_json
from unittest.mock import Mock, patch
import functions.basic.main as main

import pytest

URL = 'http://myservice.com'
USERNAME = 'user'
PASSWORD = 'pass'

EVENT_LIST_JSON = load_json('tests/basic/fixtures/sample_s3_event_list.json')
EXPECTED_S3_PATH = 's3://sourcebucket/results/myNewResults.json'

RECEIVER = {
    'url': URL,
    'username': USERNAME,
    'password': PASSWORD
}

@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    monkeypatch.setenv('RECEIVER_URL', URL)
    monkeypatch.setenv('RECEIVER_USERNAME', USERNAME)
    monkeypatch.setenv('RECEIVER_PASSWORD', PASSWORD)

@patch('functions.basic.main.notifier.notify')
def test_receiver_is_notified(mock_notifier):
    main.handle(EVENT_LIST_JSON, {})
    mock_notifier.assert_called_with(RECEIVER, EXPECTED_S3_PATH)
