import json
import re
from typing import List

from exceptions.InvalidRecords import InvalidFilename, InvalidType
from models.sheet import Sheet


class Excel:
    SCHEMA_NAME = 'reports'

    def __init__(self, filename: str, webhook: bool, sheets: List[Sheet]):
        self.filename = self.validate_filename(filename)
        self.webhook = self.validate_webhooks(webhook)
        self.sheets = self.create_sheets(sheets)

        self.log_output = []

        # Validations
        self.validate_sheets_length()

    def validate_filename(self, filename):
        pattern = r'^[a-zA-Z0-9-_]+$'
        if re.match(pattern, filename):
            return filename
        else:
            raise InvalidFilename

    def validate_webhooks(self, webhook):
        if isinstance(webhook, eval('bool')):
            return webhook
        else:
            raise InvalidType

    def validate_sheets_length(self):
        if len(self.sheets) <= 0:
            raise ValueError("Invalid sheet format, add more than 1 value")

    def create_sheets(self, sheets):
        return [Sheet(item['name'], item['columns'], item['data']) for item in sheets]

    def to_dict(self):
        return {
            'filename': self.filename,
            'webhook': self.webhook,
            'sheets': [sheet.to_dict() for sheet in self.sheets]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
