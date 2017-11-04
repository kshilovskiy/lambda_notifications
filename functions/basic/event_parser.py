def extract_s3_path(event):
    key = event['s3']['object']['key']
    bucket = event['s3']['bucket']['name']

    return f"s3://{bucket}/{key}"
