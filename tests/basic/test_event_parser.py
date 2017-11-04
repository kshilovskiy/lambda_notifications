import functions.basic.event_parser as event_parser

def test_extracts_key_and_bucket_from_s3_record():
    key, bucket = event_parser.extract_s3_key_and_bucket()
    bucket == 'bucket'
    key == 'key'
