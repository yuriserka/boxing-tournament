import logging
from uuid import uuid4


class LogIdFormatter(logging.Formatter):
    def format(self, record):
        record.logid = uuid4()
        return super().format(record)
