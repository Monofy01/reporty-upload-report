import json

import pytest

from src.exceptions.sheet_exceptions import *
from src.models.excel import Excel
from src.models.sheet import Sheet


def read_json_data(filename):
    with open(filename, 'r') as file:
        request = json.load(file)

    body = json.loads(request['body'])
    return body['excel']


def test_invalid_sheet_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/invalid_sheet_name.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidName):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


# Prueba para un caso malformado de Sheet
def test_invalid_sheets_malformed():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheets_malformed.json')
    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidSheetStructure
    with pytest.raises(InvalidSheetStructure):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_length_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_name_invalid_length.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidLengthName):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

# TODO: TEST
def test_invalid_column_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_name_invalid.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnName):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_column_name_length():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_name_length_invalid.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnNameLength):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

def test_invalid_column_type():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_type.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnTypes):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_column_data_numbers():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_data_number.json')

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidDataAndColumns):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)