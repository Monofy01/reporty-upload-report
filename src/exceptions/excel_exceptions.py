from src.utils.constants.constants import Http


class ExcelException(RuntimeError):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.message = message
        self.http_code = http_code

    def to_dict(self):
        return {
            "message": self.message,
            "http_code": self.http_code
        }


class InvalidFilename(ExcelException):
    def __init__(self):
        message = "El campo {FILENAME} solo permite caracteres alfanuméricos, guiones medios y guiones bajos"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidType(ExcelException):
    def __init__(self):
        message = "El campo de {WEBHOOK} ingresado no es una variable de tipo bool"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetLength(ExcelException):
    def __init__(self):
        message = "El campo {SHEETS} debe tener al menos un valor para poder ser procesado"
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class ReporteExistente(ExcelException):
    def __init__(self):
        message = "El reporte que se intenta carga ya ha sido generado en el sistema"
        http_code = Http.CONFLICT
        super().__init__(message, http_code)
