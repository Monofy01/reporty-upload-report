from src.utils.constants.constants import Http


class SheetException(RuntimeError):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.message = message
        self.http_code = http_code

    def to_dict(self):
        return {
            "message": self.message,
            "http_code": self.http_code
        }


class InvalidName(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructureMatch(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)

class InvalidSheetStructureName(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructureColumn(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructureData(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidLengthName(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnName(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnNameLength(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidColumnTypes(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidDataAndColumns(SheetException):
    def __init__(self, message):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)

