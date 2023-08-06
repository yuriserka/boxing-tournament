import logging
import sys
from datetime import datetime

from src.core.utils.logger.log_id_formatter import LogIdFormatter
from src.core.utils.logger.json_output_formatter import JsonOutputFormatter

date = datetime.now().strftime("%Y-%m-%d")
file_handler = logging.FileHandler(filename=f"logs/{date}.log", mode="a")
stdout_handler = logging.StreamHandler(stream=sys.stdout)
logid_formatter = LogIdFormatter(
    '%(logid)s %(asctime)s %(levelname)s: [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

stdout_handler.setFormatter(logid_formatter)
file_handler.setFormatter(JsonOutputFormatter(logid_formatter._fmt))
handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.DEBUG, handlers=handlers)


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg, exc_info=True)

    def error(self, msg):
        self.logger.error(msg, exc_info=True)
