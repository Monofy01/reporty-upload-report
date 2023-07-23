import json

from src.models.excel import Excel
from src.models.sheet import Sheet


class CreatorXlsx:
    def __init__(self, data_xlsx):
        self.excel = Excel(data_xlsx['filename'], data_xlsx['webhook'], data_xlsx['sheets'])

class CreatorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CreatorXlsx):
            return {
                'filename': obj.excel.filename,
                'webhook': obj.excel.webhook,
                'sheets': obj.excel.sheets
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
                'data': obj.data
            }
        return super().default(obj)
