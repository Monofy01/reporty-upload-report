import json

from db.dynamo_client import DynamoClient
from services.report_services import ReportService


def handler(event, context):
    request_data = json.loads(event['body'])
    excel = ReportService()
    response = excel.validate_xlsx(request_data['excel'])
    DynamoClient().insert_metadata(request_data['excel']['filename'], request_data['email'])
    return response
