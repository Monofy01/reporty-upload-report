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
        columns, data = [], []
        log_output = logs

        # VERIFICAMOS ESTRUCTURA INTERNA DE COLUMNS Y DATA
        msg1 = "La lista ingresada de [sheets.columns] debe contener unicamente listas"
        msg2 = "La lista ingresada de [sheets.data] debe contener unicamente diccionarios"

        ex1 = InvalidSheetStructureMatch(msg1).to_dict()
        ex2 = InvalidSheetStructureMatch(msg2).to_dict()
        invalid_structure = [ex1, ex2]

        if not any(ex in log_output for ex in invalid_structure):
            columns = [tuple(column) for column in sheet_dict.get('columns', []) if isinstance(column, list)]
            data = [dict(item) for item in sheet_dict.get('data', []) if len(item) == 2]

        return cls(name, columns, data, log_output)

    def __post_init__(self):
        ex1_msg = "La lista ingresada de [sheets] no contiene el campo [sheet.name]"
        ex2_msg = "La lista ingresada de [sheets] no contiene el campo [sheet.columns]"
        ex3_msg = "La lista ingresada de [sheets] no contiene el campo [sheet.data]"

        ex1 = InvalidSheetStructureName(ex1_msg).to_dict()
        ex2 = InvalidSheetStructureColumn(ex2_msg).to_dict()
        ex3 = InvalidSheetStructureData(ex3_msg).to_dict()

        log_exceptions = [ex1["message"], ex2["message"], ex3["message"]]
        log_found = any(msg in self.log_output for msg in log_exceptions)

        if not log_found:
            validations = {
                ex1_msg: [self.validate_sheet_name],
                ex2_msg: [self.validate_sheet_columns],
                ex3_msg: [self.validate_data]
            }

            for msg in log_exceptions:
                if msg in self.log_output:
                    for validation_method in validations.get(msg, []):
                        validation_method()

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
            msg = f"VALIDATIONS :: El valor [sheet.name] = [{self.name}] excede la longitud maxima"
            print(msg)
            self.log_output.append(InvalidLengthName(msg.split("VALIDATIONS :: ")[-1]).to_dict())

        # SECOND CONDITION
        pattern = r'^[a-zA-Z0-9-_]+$'
        if not re.match(pattern, self.name):
            if not InvalidSheetStructureName(
                    "La lista ingresada de [sheets] no contiene el campo [sheet.name]").to_dict() in self.log_output:
                msg = f"VALIDATIONS :: El [sheet.name] = [{self.name}] ingresado solo debe permitir caracteres " \
                      f"alfanumericos, guiones bajos y guiones medios"
                print(msg)
                self.log_output.append(InvalidName(msg.split("VALIDATIONS :: ")[-1]).to_dict())

    def validate_sheet_columns(self):
        VALID_TYPES = {'int', 'float', 'str', 'bool', 'list'}

        for c in self.columns:
            pattern = r'^[a-zA-Z0-9_]{1,12}$'
            if len(c[0]) > 13:
                msg = f"VALIDATIONS :: El valor [sheet.columns.name] = [{c[0]}] excede la longitud maxima"
                print(msg)
                self.log_output.append(InvalidColumnNameLength(msg.split("VALIDATIONS :: ")[-1]).to_dict())
            if not re.match(pattern, c[0]):
                msg = f"VALIDATIONS :: El valor [sheet.columns.name] = [{c[0]}] solo debe permitir caracteres " \
                      f"alfanuméricos y guiones bajos."
                print(msg)
                self.log_output.append(InvalidColumnName(msg.split("VALIDATIONS :: ")[-1]).to_dict())
            if not c[1].lower() in VALID_TYPES:
                msg = f"VALIDATIONS :: El valor [sheet.columns.type] = [{c[1]}] ingresado no coincide con los tipos " \
                      f"de datos definidos {'int', 'float', 'str', 'bool', 'list'}"
                print(msg)
                self.log_output.append(InvalidColumnTypes(msg.split("VALIDATIONS :: ")[-1]).to_dict())

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
                        msg = f"VALIDATIONS :: El valor [sheet.columns.type] = [{type_name.lower()}] ingresado no " \
                              f"coincide con los tipos de datos definidos {'int', 'float', 'str', 'bool', 'list'}"
                        if not InvalidColumnTypes(msg.split("VALIDATIONS :: ")[-1]).to_dict() in self.log_output:
                            self.log_output.append(InvalidColumnTypes(msg.split("VALIDATIONS :: ")[-1]).to_dict())


def validate_sheets_structure(dict_sheet):
    log_output = list()
    if 'name' not in dict_sheet:
        msg = "VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.name]"
        print(msg)
        log_output.append(InvalidSheetStructureName(msg.split("VALIDATIONS :: ")[-1]).to_dict())

    if 'columns' not in dict_sheet:
        msg = "VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.columns]"
        print(msg)
        log_output.append(InvalidSheetStructureColumn(msg.split("VALIDATIONS :: ")[-1]).to_dict())
    else:
        if not all(isinstance(item, list) for item in dict_sheet['columns']):
            msg = "VALIDATIONS :: La lista ingresada de [sheets.columns] debe contener unicamente listas"
            print(msg)
            log_output.append(InvalidSheetStructureMatch(msg.split("VALIDATIONS :: ")[-1]).to_dict())

    if 'data' not in dict_sheet:
        msg = "VALIDATIONS :: La lista ingresada de [sheets] no contiene el campo [sheet.data]"
        print(msg)
        log_output.append(InvalidSheetStructureData(msg.split("VALIDATIONS :: ")[-1]).to_dict())
    else:
        if not all(isinstance(item, list) for item in dict_sheet['columns']):
            msg = "VALIDATIONS :: La lista ingresada de [sheets.data] debe contener unicamente diccionarios"
            print(msg)
            log_output.append(InvalidSheetStructureMatch(msg.split("VALIDATIONS :: ")[-1]).to_dict())
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
