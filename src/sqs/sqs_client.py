import json

import boto3

from src.config.enviroments import ENVS


class SQSClient:
    def __init__(self):
        self.data = ""

    @staticmethod
    def send_message(message):
        sqs_client = boto3.client('sqs')
        message_attributes = {
            'MessageType': {
                'DataType': 'String',
                'StringValue': 'JSON'
            }
        }

        return sqs_client.send_message(QueueUrl=ENVS.SQS_URL,
                                       MessageBody=json.dumps(message),
                                       MessageAttributes=message_attributes)
