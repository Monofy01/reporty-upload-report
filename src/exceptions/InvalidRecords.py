from src.utils.constants.constants import Http


class InvalidFilename(Exception):
    def __init__(self):
        self.message = "El campo {FILENAME} solo permite caracteres alfanuméricos, guiones medios y guiones bajos"
        self.http_code = Http.BAD_REQUEST

class InvalidType(Exception):
    def __init__(self):
        self.message = "El campo de {WEBHOOK} ingresado no es una variable de tipo bool"
        self.http_code = Http.BAD_REQUEST

class InvalidSheetLength(Exception):
    def __init__(self):
        self.message = "El campo {SHEETS} debe tener al menos un valor para poder ser procesado"
        self.http_code = Http.BAD_REQUEST
