import json

from src.exceptions.InvalidRecords import InvalidColumnTypes
from src.services.creator_xlsx import CreatorXlsx
from src.sqs.sqs_client import SQSClient


class ReportService:
    def __init__(self):
        self.creator_excel = None

    def validate_xlsx(self, request_json):
        try:
            self.creator_excel = CreatorXlsx(request_json)
            SQSClient.send_message(self.creator_excel.to_json())

            return {
                'statusCode': 200,
                'body': json.dumps("El archivo [] se ha mandado correctamente a procesar")
            }
        except InvalidColumnTypes as e:
            print("ERROR EXCEPTION")
            return {
                'statusCode': 400,
                'body': json.dumps(request_json),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
