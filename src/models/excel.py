import dataclasses
import re
from typing import List

from src.exceptions.excel_exceptions import *
from src.models.sheet import Sheet


@dataclasses.dataclass
class Excel:
    filename: str
    webhook: str
    sheets: List[Sheet]
    log_output: list = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.validate_filename()
        self.validate_webhooks()
        self.validate_sheets_length()

    def to_dict(self):
        # Convierte la instancia de Excel en un diccionario
        excel_dict = {
            "filename": self.filename,
            "webhook": self.webhook,
            "sheets": [sheet.__dict__ for sheet in self.sheets],
            "log_output": self.log_output
        }
        return excel_dict

    # VALIDATIONS
    def validate_filename(self):
        pattern = r'^[a-zA-Z0-9-_]+$'
        if not re.match(pattern, self.filename):
            print(f"VALIDATIONS :: El [filename] = [{self.filename}] ingresado solo debe permitir caracteres "
                  f"alfanumericos, guiones bajos y guiones medios")
            self.log_output.append(InvalidFilename().to_dict())

    def validate_webhooks(self):
        if not isinstance(self.webhook, eval('bool')):
            print(f"VALIDATIONS :: El [webhook] = [{self.webhook}] ingresado ingresado solo debe permitir valores de tipo bool ['true', 'false']")
            self.log_output.append(InvalidType().to_dict())

    def validate_sheets_length(self):
        if len(self.sheets) <= 0:
            print(f"VALIDATIONS :: La lista ingresada de [sheets] debe contener al menos un valor para ser valida")
            self.log_output.append(InvalidSheetLength().to_dict())
