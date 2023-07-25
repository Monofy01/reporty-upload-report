import dataclasses
import re
from typing import Dict, List, Tuple

from src.exceptions.sheet_exceptions import *


@dataclasses.dataclass
class Sheet:
    name: str
    columns: List[Tuple]
    data: List[Dict]
    data_invalid: List[Dict] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, sheet_dict: Dict) -> 'Sheet':
        validate_sheets_structure(sheet_dict)
        name = sheet_dict.get('name', '')
        columns = [tuple(column) for column in sheet_dict.get('columns', [])]
        data = [dict(item) for item in sheet_dict.get('data', [])]

        return cls(name, columns, data)

    def __post_init__(self):
        self.validate_sheet_name()
        self.validate_sheet_columns()
        self.validate_data()

    def to_dict(self):
        # Convierte la instancia de Sheet en un diccionario
        sheet_dict = {
            "name": self.name,
            "columns": self.columns,
            "data": self.data,
            "data_invalid": self.data_invalid
        }
        return sheet_dict

    # VALIDATIONS

    def validate_sheet_name(self):
        # FIRST CONDITION
        if len(self.name) > 13:
            print("VALIDATIONS :: El valor [sheet.name] excede la longitud maxima")
            raise InvalidLengthName

        # SECOND CONDITION
        pattern = r'^[a-zA-Z0-9-_]{1,12}$'
        if not re.match(pattern, self.name):
            print("VALIDATIONS :: El [sheet.name] ingresado no coincide con los parametros de validación")
            raise InvalidName

    def validate_sheet_columns(self):
        VALID_TYPES = {'int', 'float', 'str', 'bool', 'list'}

        for c in self.columns:
            # pattern = r'^[a-zA-Z0-9_]{1,12}$' # TODO: RECORDAR CAMBIAR ESTO SI LO PERMITEN
            pattern = r'^[a-zA-Z0-9-_]{1,12}$'
            if len(c[0]) > 13:
                print("VALIDATIONS :: El valor [sheet.columns.name] excede la longitud maxima")
                raise InvalidColumnNameLength
            if not re.match(pattern, c[0]):
                print(
                    "VALIDATIONS :: El valor [sheet.columns.name] ingresado no coincide con los parametros de validación")
                raise InvalidColumnName
            if not c[1].lower() in VALID_TYPES:  # TODO: Si no se permiten MAYUS, eliminar lower()
                print(
                    "VALIDATIONS :: El valor [sheet.columns.type] ingresado no coincide con los tipos de datos definidos {'int', 'float', 'str', 'bool', 'list'}")
                raise InvalidColumnTypes

    def validate_data(self):
        VALID_TYPES = {'int', 'float', 'str', 'bool', 'list'}

        for index, row in enumerate(self.data):
            # VERIFICAMOS QUE EL NUMERO DE COLUMNAS Y DATOS A EVALUAR SEA EL MISMO
            if not len(self.columns) == len(row):
                raise InvalidDataAndColumns

            # no n*n, por si crece
            index_column = 0
            index_data = 0
            is_compatible = False

            # SE VERIFICA DE UNO EN UNO LA VALIDEZ DE LA FILA
            while not is_compatible:
                name_column = self.columns[index_column][0]  # OBTENEMOS EL NOMBRE DE LA COLUMNA
                type_name = self.columns[index_column][1]  # OBTENEMOS EL TIPO DE LA COLUMNA
                real_value = row[name_column]  # OBTENEMOS EL DATO REAL QUE SE QUIERE INGRESAR EN LA COLUMNA

                index_column = index_column + 1
                index_data = index_data + 1

                if index_column == len(self.columns) and index_data == len(row):
                    is_compatible = True

                # REALIZAMOS LA EVALUACION DEL TIPO DE DATO DE LA COLUMNA CON EL VALOR REAL
                if not isinstance(real_value, eval(type_name)):
                    self.data_invalid.append(self.data[index])
                    self.data.pop(index)
                    # raise InvalidData

def validate_sheets_structure(dict_sheet):
    if 'name' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.name]")
        raise InvalidSheetStructure
    if 'columns' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.columns]")
        raise InvalidSheetStructure
    if 'data' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.data]")
        raise InvalidSheetStructure

