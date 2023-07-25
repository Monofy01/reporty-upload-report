import json

from src.models.excel import Excel
from src.models.sheet import Sheet


class CreatorXlsx:
    def __init__(self, data_xlsx):
        self.excel = Excel(data_xlsx['excel']['filename'],
                           data_xlsx['excel']['webhook'],
                           data_xlsx['excel']['sheets'])
        self.email = data_xlsx['email']

