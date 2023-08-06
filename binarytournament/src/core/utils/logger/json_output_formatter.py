import logging
import json


class JsonOutputFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({k: v for k, v in record.__dict__.items()})
