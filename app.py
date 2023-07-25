import json
import re

from src.exceptions.InvalidRecords import InvalidFilename
from src.exceptions.excel_exceptions import ExcelException
from src.exceptions.sheet_exceptions import SheetException
from src.models.excel import Excel
from src.models.sheet import Sheet
from src.services.report_services import ReportService


def handler(event, context):
    try:
        # SECCION DE DECODING
        print(f"REQUEST :: {event}")
        print(f"BODY :: {event['body']}")
        body = json.loads(event['body'])
        excel_data = body['excel']
        email_data = body['email']

        # SECCION DE PROCESAMIENTO
        excel_object = Excel(
            filename=excel_data['filename'],
            webhook=excel_data['webhook'],
            sheets=[Sheet.from_dict(item) for item in excel_data['sheets']]
        )
        # ReportService.upload_report(excel_object, email_data)
    except ExcelException as ee:
        print(f"ERROR :: Ha ocurrido un error de tipo EXCEL")
        return {
            'statusCode': ee.http_code,
            'body': json.dumps({
                'message': ee.message,
                'code': ee.http_code,
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except SheetException as se:
        print(f"ERROR :: Ha ocurrido un error de tipo SHEET")
        return {
            'statusCode': se.http_code,
            'body': json.dumps({
                'message': se.message,
                'code': se.http_code,
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except json.JSONDecodeError as e:
        print(f"ERROR :: Ha ocurrido un error al intentar decodificar el mensaje entrante :: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': "Ha ocurrido un error al intentar decodificar el mensaje entrante",
                'code': 400,
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        print(f"ERROR :: Ha ocurrido un error generico :: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Ha ocurrido un error inesperado dentro de la aplicación, por favor consulte al "
                           f"administrador :: ERROR {e}",
                'code': 500,
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
