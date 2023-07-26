import json

import pytest

from src.exceptions.sheet_exceptions import *
from src.models.excel import Excel
from src.models.sheet import Sheet


def read_json_data(filename, alternative):
    with open(filename, 'r') as file:
        request = json.load(file)
    if alternative:
        return request['excel']
    else:
        body = json.loads(request['body'])
        return body['excel']


def test_invalid_sheet_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/invalid_sheet_name.json', True)

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
    excel_data = read_json_data('usecases/sheet/sheets_malformed.json', True)
    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidSheetStructure
    with pytest.raises(InvalidSheetStructure):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_length_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_name_invalid_length.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidLengthName):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_column_name():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_name_invalid.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnName):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


# TODO: ESTA DE MAS
def test_invalid_column_name_length():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_name_length_invalid.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnNameLength):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_invalid_column_type():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/sheet_column_type.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']

    # Verifica si se lanza la excepción InvalidName
    with pytest.raises(InvalidColumnTypes):
        sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
        excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


# def test_invalid_column_data_numbers():
#     # Lee los datos del archivo JSON
#     excel_data = read_json_data('usecases/sheet/sheet_column_data_number.json', True)
#
#     # Ingresa un valor inválido para el filename aquí
#     filename = excel_data['filename']
#     webhook = excel_data['webhook']
#
#     # Verifica si se lanza la excepción InvalidName
#     with pytest.raises(InvalidDataAndColumns):[[{"column_1": "int", "column_2": "bool"}, {"column_1": 1, "column_2": True, "column_3": [1, 2, 3]}, {"column_1": 1, "column_2": True, "column_3": [1, 2, 3]}]]
#         sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
#         excel = Excel(filename=filename, webhook=webhook, sheets=sheets)


def test_data_no_match_columns():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/data_no_match_column.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
    excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

    row_descartada = {
        "column_1": 1,
        "column_N": "Una Cadena"
    }

    row_correcta = {
        "column_1": 19,
        "column_2": False,
        "column_N": "Otra Cadena"
    }

    valores_correctos = []
    valores_descartados = []

    for s in excel.sheets:
        valores_correctos = s.data
        valores_descartados = s.data_invalid

    # Verifica si el objeto Excel fue creado correctamente sin lanzar excepciones
    assert isinstance(excel, Excel)
    assert row_correcta in valores_correctos
    assert row_descartada in valores_descartados


def test_data_no_match_columns():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/data_no_match_column.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
    excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

    row_descartada = {
        "column_1": 1,
        "column_N": "Una Cadena"
    }

    row_correcta = {
        "column_1": 19,
        "column_2": False,
        "column_N": "Otra Cadena"
    }

    valores_correctos = []
    valores_descartados = []

    for s in excel.sheets:
        valores_correctos.extend(s.data)
        valores_descartados.extend(s.data_invalid)

    # Verifica si el objeto Excel fue creado correctamente sin lanzar excepciones
    assert isinstance(excel, Excel)
    assert row_correcta in valores_correctos
    assert row_descartada in valores_descartados


def test_data_no_match_data():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/data_no_match_data.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
    excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

    row_descartada = [
        {
            "column_1": 1,
            "column_2": False,
            "column_N": "Una Cadena"
        },
        {
            "column_1": 19,
            "column_2": False,
            "column_N": "Otra Cadena"
        }
    ]

    valores_correctos = []
    valores_descartados = []

    for s in excel.sheets:
        if len(s.data) != 0:
            valores_correctos.extend(s.data)
        if len(s.data_invalid) != 0:
            valores_descartados.extend(s.data_invalid)

    # Verifica si el objeto Excel fue creado correctamente sin lanzar excepciones
    assert isinstance(excel, Excel)
    assert len(valores_correctos) == 0
    assert row_descartada == valores_descartados

def test_data_invalid_type():
    # Lee los datos del archivo JSON
    excel_data = read_json_data('usecases/sheet/data_invalida.json', True)

    # Ingresa un valor inválido para el filename aquí
    filename = excel_data['filename']
    webhook = excel_data['webhook']
    sheets = [Sheet.from_dict(item) for item in excel_data['sheets']]
    excel = Excel(filename=filename, webhook=webhook, sheets=sheets)

    row_descartada = {
        "column_1": "CADENA_ERROR",
        "column_2": False
    }

    row_correcta = {
        "column_1": 1,
        "column_2": True
    }

    valores_correctos = []
    valores_descartados = []

    for s in excel.sheets:
        valores_correctos.extend(s.data)
        valores_descartados.extend(s.data_invalid)

    # Verifica si el objeto Excel fue creado correctamente sin lanzar excepciones
    assert isinstance(excel, Excel)
    assert row_correcta in valores_correctos
    assert row_descartada in valores_descartados
