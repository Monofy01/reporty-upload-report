from src.utils.constants.constants import Http


class StructureException(RuntimeError):
    def __init__(self, message, http_code):
        super().__init__(message)
        self.message = message
        self.http_code = http_code

    def to_dict(self):
        return {
            "message": self.message,
            "http_code": self.http_code
        }

class InvalidSheetStructureMatchColumns(StructureException):
    def __init__(self, message='La lista ingresada de [sheets.columns] debe contener unicamente listas'):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)

class InvalidSheetStructureMatchData(StructureException):
    def __init__(self, message='La lista ingresada de [sheets.data] debe contener unicamente diccionarios'):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructureName(StructureException):
    def __init__(self, message='La lista ingresada de [sheets] no contiene el campo [sheet.name]'):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)

class InvalidSheetStructureColumn(StructureException):
    def __init__(self, message='La lista ingresada de [sheets] no contiene el campo [sheet.columns]'):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)


class InvalidSheetStructureData(StructureException):
    def __init__(self, message='La lista ingresada de [sheets] no contiene el campo [sheet.data]'):
        message = message
        http_code = Http.BAD_REQUEST
        super().__init__(message, http_code)



