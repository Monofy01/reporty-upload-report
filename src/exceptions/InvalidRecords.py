class InvalidFilename(Exception):
    def __init__(self):
        self.message = "Solo se deben permitir caracteres alfanuméricos, guion medio y guion bajo"
        self.http_code = 400


class InvalidName(Exception):
    def __init__(self):
        self.message = "Solo se deben permitir caracteres alfanuméricos, guion medio y guion bajo"
        self.http_code = 400


class InvalidColumnName(Exception):
    def __init__(self):
        self.message = "El nombre de la columna solo deben permitir caracteres alfanuméricos y guion bajo"
        self.http_code = 400


class InvalidColumnTypes(Exception):
    def __init__(self):
        self.message = "int, float, str, bool, list; cualquier otro tipo de dato especificado deberá ser descartado"
        self.http_code = 400



class InvalidType(Exception):
    def __init__(self):
        self.message = "Only bool type for this field"
        self.http_code = 400


class InvalidColumnData(Exception):
    def __init__(self):
        self.message = "Sus campos deberán coincidir con las columnas especificadas en columns, de hacer falta, contener un campo distinto o el valor no corresponda con el tipo"
        self.http_code = 400


class InvalidDataAndColumns(Exception):
    def __init__(self):
        self.message = "El número de columnas y el número de campos ingresados en cada objeto de dato debería ser el mismo"
        self.http_code = 400

class ReporteExistente(Exception):
    def __init__(self):
        self.message = "El reporte que quieres subir ya ha sido generado"
        self.http_code = 409