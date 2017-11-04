from tests.helpers import load_json
import functions.basic.event_parser as event_parser

EVENT_JSON = load_json('tests/basic/fixtures/sample_s3_event.json')

def test_extracts_path_to_file_from_s3_event():
    path = event_parser.extract_s3_path(EVENT_JSON)

    assert path == 's3://sourcebucket/results/myNewResults.json'
