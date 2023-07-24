import json

from src.db.dynamo_client import DynamoClient
from src.exceptions.InvalidRecords import InvalidColumnTypes, InvalidFilename, InvalidType, InvalidColumnName, \
    InvalidDataAndColumns, ReporteExistente, InvalidName
from src.services.creator_xlsx import CreatorXlsx, CreatorEncoder
from src.sqs.sqs_client import SQSClient


class ReportService:
    def __init__(self):
        self.creator_excel = None

    def validate_xlsx(self, request_json):
        try:
            self.creator_excel = CreatorXlsx(request_json)
            DynamoClient().insert_metadata(request_json['excel']['filename'], request_json['email'])
            SQSClient.send_message(json.dumps(self.creator_excel, cls=CreatorEncoder))


            response = {
                'message': f"El archivo {request_json['excel']['filename']} se ha mandado correctamente a procesar"
            }
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                },
                'body': json.dumps(response),
            }
        except ValueError as e:
            print("ERROR EXCEPTION")
            return {
                'statusCode': 400,
                'body': json.dumps(str(e)),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
        except (InvalidColumnTypes, InvalidName, InvalidFilename, InvalidType, InvalidColumnName, InvalidColumnTypes, InvalidDataAndColumns, ReporteExistente) as e:
            response = {
                'message': e.message,
                'code': e.http_code,
            }
            return {
                'statusCode': response['code'],
                'body': json.dumps(response),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
