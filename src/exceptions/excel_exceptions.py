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
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidType(ExcelException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetLength(ExcelException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class ReporteExistente(ExcelException):
    def __init__(self, message):
        message = message
        http_code = Http.CONFLICT
        super().__init__(message, http_code)
