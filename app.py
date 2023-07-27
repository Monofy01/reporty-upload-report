import json

from src.exceptions.excel_exceptions import ReporteExistente
from src.models.excel import Excel
from src.models.sheet import Sheet
from src.services.report_services import ReportService
from src.utils.constants.constants import Http


def handler(event, context):
    try:
            # SECCION DE DECODING
            print(f"REQUEST :: {event}")
            body = json.loads(event['body'])
            excel_data = body['excel']
            email_data = body['email']

            log_output = list()

            # SECCION DE PROCESAMIENTO
            excel_object = Excel(
                filename=excel_data['filename'],
                webhook=excel_data['webhook'],
                sheets=[Sheet.from_dict(item) for item in excel_data['sheets']]
            )

            # ACUMULACION DE ERRORES
            log_output.extend(excel_object.log_output)
            for s in excel_object.sheets:
                if len(s.log_output) > 0:
                    log_output.append(s.log_output)

            if len(log_output) > 0:
                # print(F"ERRORES FINALES {log_output}")
                return {
                    'statusCode': Http.UNPROCESSABLE,
                    'body': log_output,
                    'headers': {
                        'Content-Type': 'application/json'
                    }
                }
            else:
                # SECCION DE PROCESAMIENTO
                try:
                    ReportService.upload_report(excel_object, email_data)
                    return {
                        'statusCode': Http.SUCCESS,
                        'body': json.dumps({
                            'message': f'Se ha enviado exitosamente el reporte con el nombre {excel_object.filename}',
                            'code': Http.SUCCESS,
                        }),
                        'headers': {
                            'Content-Type': 'application/json'
                        }
                    }
                except Exception as e:
                    log_output.append(ReporteExistente().to_dict())
                    return {
                        'statusCode': Http.UNPROCESSABLE,
                        'body': log_output,
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
