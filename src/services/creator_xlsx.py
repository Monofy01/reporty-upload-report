import json

from src.models.excel import Excel
from src.models.sheet import Sheet


class CreatorXlsx:
    def __init__(self, data_xlsx):
        self.excel = Excel(data_xlsx['excel']['filename'], data_xlsx['excel']['webhook'], data_xlsx['excel']['sheets'])
        self.email = data_xlsx['email']

class CreatorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CreatorXlsx):
            return {
                'excel': obj.excel,
                'email': obj.email
            }
        if isinstance(obj, Excel):
            return {
                'filename': obj.filename,
                'webhook': obj.webhook,
                'sheets': obj.sheets
            }
        if isinstance(obj, Sheet):
            return {
                'name': obj.name,
                'columns': obj.columns,
                'data': obj.data,
                'data_invalid': obj.data_invalid
            }
        if hasattr(obj, 'email'):
            return obj.email
        return super().default(obj)
