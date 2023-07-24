import json

from src.db.dynamo_client import DynamoClient
from src.services.report_services import ReportService


def handler(event, context):
    print(f"REQUEST :: {event}")
    try:
        request_data = json.loads(event['body'])
        excel = ReportService()
        response = excel.validate_xlsx(request_data['excel'], request_data['email'])
        return response
    except Exception as e:
        print(f"ERROR :: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(e),
            'headers': {
                'Content-Type': 'application/json'
            }
        }