import json
from json import JSONDecodeError

import pytest

from src.exceptions.sheet_exceptions import *
from src.models.excel import Excel
from src.exceptions.excel_exceptions import *
from src.models.sheet import Sheet


def read_json_data(filename):
    with open(filename, 'r') as file:
        request = json.load(file)

    body = json.loads(request['body'])
    return body['excel']

# Prueba para un caso válido de Excel
def test_valid_excel():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/excel/valid_report.json')

    # Obtén los valores de prueba del archivo JSON
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]

    excel = Excel(filename=filename, webhook=webhook, sheets=sheets)
    # Verifica si el objeto Excel fue creado correctamente sin lanzar excepciones
    assert isinstance(excel, Excel)

# Prueba para un caso de filename inválido
def test_invalid_filename():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/excel/invalid_report_name.json')

    # Obtén los valores de prueba del archivo JSON
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]

    # Verifica si se lanza la excepción InvalidFilename
    with pytest.raises(InvalidFilename):
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

# Prueba para un caso de webhook inválido
def test_invalid_webhook():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/excel/invalid_report_webhook.json')

    # Obtén los valores de prueba del archivo JSON
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]

    # Verifica si se lanza la excepción InvalidType
    with pytest.raises(InvalidType):
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

# Prueba para un caso de sheets vacío
def test_invalid_sheets_length():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/excel/sheets_empty.json')

    # Obtén los valores de prueba del archivo JSON
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]

    # Verifica si se lanza la excepción InvalidSheetLength
    with pytest.raises(InvalidSheetLength):
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


# Prueba para un caso custom
def test_custom_1():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/excel/custom_1.json')

    # Obtén los valores de prueba del archivo JSON
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción Exception
    with pytest.raises(InvalidDataAndColumns):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)
