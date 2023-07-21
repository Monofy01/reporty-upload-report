import json

from models.excel import Excel


class CreatorXlsx:
    def __init__(self, data_xlsx):
        self.excel = Excel(data_xlsx['filename'], data_xlsx['webhook'], data_xlsx['sheets'])

    def to_dict(self):
        return {
            'excel': self.excel.to_dict()
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
