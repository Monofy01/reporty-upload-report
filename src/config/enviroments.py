import os


class ENVS:
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    SQS_URL = os.environ.get('SQS_URL')
    DYNAMO_TABLE_METADATA = os.environ.get('DYNAMO_TABLE_METADATA')

    def __int__(self):
        pass