from src.utils.constants.constants import Http


class SheetException(RuntimeError):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.message = message
        self.http_code = http_code


class InvalidName(SheetException):
    def __init__(self):
        message = "El campo {SHEETS.NAME} solo debe permitir caracteres alfanumericos, guiones bajos y guiones medios"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructure(SheetException):
    def __init__(self):
        message = "El campo {SHEETS} debe contener estos 3 campos [name{text}, columns{lista} y data{lista}]"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidLengthName(SheetException):
    def __init__(self):
        message = "El campo {NAME} excede la longitud maxima de 12 caracteres permitida"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnName(SheetException):
    def __init__(self):
        message = "El campo de {SHEETS.COLUMNS} en su primer elemento [nombre_columna] no coincide con los parametros establecidos en las validaciones"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnNameLength(SheetException):
    def __init__(self):
        message = "El campo de {SHEETS.COLUMNS} en su primer elemento [nombre_columna] excede el tamaño permitido de 12 caracteres"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnTypes(SheetException):
    def __init__(self):
        message = "El campo de {SHEETS.COLUMNS} en su primer elemento [nombre_columna] no coincide con los parametros establecidos en las validaciones"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidDataAndColumns(SheetException):
    def __init__(self):
        message = "El número de columnas y el número de datos ingresados, no coincide"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)

# DEPRECATED
# class InvalidData(SheetException):
#     def __init__(self):
#         message = "El valor del dato ingresado no coincide con el valor especificado para esa columna"
#         http_code = Http.BAD_REQUEST
#         super().__init__(message, http_code)
