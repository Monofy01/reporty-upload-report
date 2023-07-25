import json

import boto3

from src.config.enviroments import ENVS


class SQSClient:
    def __init__(self):
        pass

    @staticmethod
    def send_message(excel_json, email_data):
        sqs_client = boto3.client('sqs')
        sqs_message = {
            'email': email_data,
            'excel': excel_json
        }

        return sqs_client.send_message(QueueUrl=ENVS.SQS_URL,
                                       MessageBody=json.dumps(excel_json))
