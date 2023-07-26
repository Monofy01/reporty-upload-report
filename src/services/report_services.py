import json

from src.db.dynamo_client import DynamoClient
from src.sqs.sqs_client import SQSClient


class ReportService:


    @staticmethod
    def upload_report(excel_object, email_data):
        excel_json = json.dumps(excel_object.to_dict())
        DynamoClient.insert_metadata(excel_object.filename, email_data)
        SQSClient.send_message(excel_json, email_data)






