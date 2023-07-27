import datetime
import hashlib
import logging

import boto3
import pytz

from src.config.enviroments import ENVS
from src.exceptions.excel_exceptions import ReporteExistente


class DynamoClient:
    def __init__(self):
        pass

    @staticmethod
    def insert_metadata(filename, email):
        dynamodb = boto3.client('dynamodb')

        current_datetime = datetime.datetime.now(pytz.timezone('UTC'))
        iso_format_date = current_datetime.isoformat()
        md5_hash = hashlib.md5(f'{filename}'.encode()).hexdigest()

        metadata_xlsx = [
            {
                'Put': {
                    'TableName': ENVS.DYNAMO_TABLE_METADATA,
                    'Item': {
                        'id': {'S': md5_hash},
                        'name': {'S': f'{filename}'},
                        'status': {'S': 'En Proceso'},
                        'user_owner': {'S': email},
                        'users_allowed': {'SS': [email]},
                        'created_at': {'S': iso_format_date}
                    },
                    'ConditionExpression': 'attribute_not_exists(id)'
                }
            },
            {
                'Put': {
                    'TableName': ENVS.DYNAMO_TABLE_METADATA,
                    'Item': {
                        'id': {'S': 'name#' + f'{filename}'},
                    },
                    'ConditionExpression': 'attribute_not_exists(id)'
                }
            }
        ]

        try:
            dynamodb.transact_write_items(TransactItems=metadata_xlsx)
            print("INFO :: La metadata ha sido insertada correctamente en las tablas de DynamoDB")
        except Exception as e:
            print(f"ERROR :: Ha ocurrido un error en la generacion del reporte :: {e}")
            print(f"VALIDATIONS :: El [filename] = [{filename}] ingresado ya ha sido generado como un reporte valido")
            raise ReporteExistente
