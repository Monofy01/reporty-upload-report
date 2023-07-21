import json
from typing import Tuple, List
import re

from src.exceptions.InvalidRecords import InvalidName, InvalidColumnName, InvalidColumnTypes, InvalidDataAndColumns


class Sheet:
    def __init__(self, name: str, columns: Tuple[str, str], data: List[dict]):
        # TODO: REVISAR VERIFICACIONES
        self.data = data
        self.data_invalid = list()
        self.union_validations(name, columns)
        self.name = name
        self.columns = tuple(columns)

    def union_validations(self, name, columns):
        self.validate_name(name)
        self.validate_columns(columns)
        self.validate_data(columns)

    def validate_name(self, name):
        pattern = r'^[a-zA-Z0-9-_]{1,12}$'
        if re.match(pattern, name):
            return name
        else:
            raise InvalidName

    def validate_columns(self, columns):
        valid_types = {'int', 'float', 'str', 'bool', 'list'} # TODO: TIENE QUE SER CONSTANTE
        for col in columns:
            pattern = r'^[a-zA-Z0-9-_]{1,12}$'
            if not re.match(pattern, col[0]):
                raise InvalidColumnName
            if not col[1] in valid_types:
                raise InvalidColumnTypes

    def validate_data(self, columns):
        for index, row in enumerate(self.data):
            valid_types = {'int', 'float', 'str', 'bool', 'list'}
            if not len(columns) == len(row):
                # TODO: AÑADIR EXCEPCION CUANDO NO CORRESPONDAN, SE EVITA EL INSERT Y SE ANEXA LOG DE SALIDA
                raise InvalidDataAndColumns

            # no n*n, por si crece
            index_column = 0
            index_data = 0
            is_compatible = False

            while not is_compatible:
                name_column = columns[index_column][0]
                type_name = columns[index_column][1]
                real_value = row[name_column]
                index_column = index_column + 1
                index_data = index_data + 1

                if index_column == len(columns) and index_data == len(row):
                    is_compatible = True

                if not isinstance(real_value, eval(type_name)):
                    self.data_invalid.append(self.data[index])
                    self.data.pop(index)

    def to_dict(self):
        return {
            'name': self.name,
            'columns': self.columns,
            'data': self.data,
            'data_invalid': self.data_invalid
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
