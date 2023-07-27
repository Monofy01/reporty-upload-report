import dataclasses
import re
from typing import Dict, List, Tuple

from src.exceptions.sheet_exceptions import *


@dataclasses.dataclass
class Sheet:
    name: str
    columns: List[Tuple]
    data: List[Dict]
    log_output: List
    data_invalid: List[Dict] = dataclasses.field(default_factory=list)


    @classmethod
    def from_dict(cls, sheet_dict: Dict) -> 'Sheet':
        logs = validate_sheets_structure(sheet_dict)
        name = sheet_dict.get('name', '')
        columns = [tuple(column) for column in sheet_dict.get('columns', [])]
        data = [dict(item) for item in sheet_dict.get('data', [])]
        log_output = logs

        return cls(name, columns, data, log_output)

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
            print(f"VALIDATIONS :: El valor [sheet.name] = [{self.name}] excede la longitud maxima")
            self.log_output.append(InvalidLengthName().to_dict())

        # SECOND CONDITION
        pattern = r'^[a-zA-Z0-9-_]+$'
        if not re.match(pattern, self.name):
            if not InvalidSheetStructureName().to_dict() in self.log_output:
                print(f"VALIDATIONS :: El [sheet.name] = [{self.name}] ingresado solo debe permitir caracteres "
                  f"alfanumericos, guiones bajos y guiones medios")
                self.log_output.append(InvalidName().to_dict())

    def validate_sheet_columns(self):
        VALID_TYPES = {'int', 'float', 'str', 'bool', 'list'}

        for c in self.columns:
            pattern = r'^[a-zA-Z0-9_]{1,12}$'
            if len(c[0]) > 13:
                print(f"VALIDATIONS :: El valor [sheet.columns.name] = [{c[0]}] excede la longitud maxima")
                self.log_output.append(InvalidColumnNameLength().to_dict())
            if not re.match(pattern, c[0]):
                print(
                    f"VALIDATIONS :: El valor [sheet.columns.name] = [{c[0]}] solo debe permitir caracteres "
                    f"alfanuméricos y guiones bajos.")
                self.log_output.append(InvalidColumnName().to_dict())
            if not c[1].lower() in VALID_TYPES:
                print(
                    f"VALIDATIONS :: El valor [sheet.columns.type] = [{c[1]}] ingresado no coincide con los tipos de datos definidos {'int', 'float', 'str', 'bool', 'list'}")
                self.log_output.append(InvalidColumnTypes().to_dict())

    def validate_data(self):
        VALID_TYPES = {'int', 'float', 'str', 'bool', 'list'}

        real_data = list(enumerate(self.data))

        for index, row in real_data:
            # VERIFICAMOS QUE EL NUMERO DE COLUMNAS Y DATOS A EVALUAR SEA EL MISMO
            if not validate_match_dc(self.columns, row):
                self.data_invalid.append(real_data[index][1])
                self.data.remove(row)
            else:
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
                    try:
                        if not isinstance(real_value, eval(type_name.lower())):
                            self.data_invalid.append(real_data[index][1])
                            self.data.remove(row)
                    except Exception as e:
                        if not InvalidColumnTypes().to_dict() in self.log_output:
                            self.log_output.append(InvalidColumnTypes().to_dict())

def validate_sheets_structure(dict_sheet):
    log_output = list()
    if 'name' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.name]")
        log_output.append(InvalidSheetStructureName().to_dict())
    if 'columns' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.columns]")
        log_output.append(InvalidSheetStructureColumn().to_dict())
    if 'data' not in dict_sheet:
        print("VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.data]")
        log_output.append(InvalidSheetStructureData().to_dict())
    return log_output
def validate_match_columns_data(columns, row):
    for c in columns:
        column_name = c[0]
        if column_name in row.keys():
            continue
        else:
            return False
    return True

def validate_match_data_columns(columns, row):
    for k, v in row.items:
        row_name = k
        for c in columns:
            if row_name in columns[0]:
                continue
            else:
                return False
    return True

def validate_match_dc(columns, row):
    columns_set = set()
    rows_set = set()
    for c in columns:
        columns_set.add(c[0])
    for k in row.keys():
        rows_set.add(k)
    return columns_set == rows_set
