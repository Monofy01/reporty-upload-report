class InvalidFilename(Exception):
    def __str__(self) -> str:
        return """Solo se deben permitir caracteres alfanuméricos, guion medio y guion bajo"""


class InvalidName(Exception):
    """Solo se deben permitir caracteres alfanuméricos, guion medio y guion bajo"""
    pass


class InvalidColumnName(Exception):
    """El nombre de la columna solo deben permitir caracteres alfanuméricos y guion bajo"""
    pass


class InvalidColumnTypes(Exception):
    def __init__(self):
        self.message = 'int, float, str, bool, list; cualquier otro tipo de dato especificado deberá ser descartado'

class InvalidType(Exception):
    def __init__(self):
        self.message = 'Only bool type for this field'

class InvalidColumnData(Exception):
    """sus campos deberán coincidir con las columnas especificadas en columns , de hacer falta,contener un campo distinto o el valor no corresponda con el tipo"""
    pass

class InvalidDataAndColumns(Exception):
    """El numero de columnas y el numero de campos ingresados en cada objeto de dato deberia ser el mismo"""
    pass
