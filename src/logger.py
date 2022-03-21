import json
import logging
import os
import sys
import traceback
from datetime import datetime


# Following https://github.com/GuildEducationInc/guild-loggers-python pattern
def is_serializable(x):
    try:
        json.dumps(x)
        return True
    except Exception:
        return False


class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            "env": os.environ.get("STAGE"),
            "filename": record.filename,
            "level": record.levelname.lower(),
            "time": self._to_iso8601(record.created),
            "requestId": getattr(record, "requestId", None),
            "academicPartnerId": getattr(record, "academicPartnerId", None),
            "employerId": getattr(record, "employerId", None),
            "currentUser": getattr(record, "currentUser", None),
        }

        if hasattr(record, "lineno") and record.lineno:
            data["line_number"] = record.lineno

        if hasattr(record, "func") and record.func:
            data["function"] = record.func

        if hasattr(record, "msg") and record.msg and is_serializable(record.msg):
            data["message"] = record.msg

        if hasattr(record, "args") and record.args and is_serializable(record.args):
            data["metadata"] = record.args

        if (
                hasattr(record, "exc_info")
                and record.exc_info is not None
                and record.exc_info != (None, None, None)
        ):
            exc_type, exc_value, exc_traceback = record.exc_info
            exc_info = {
                "error": {
                    "type": exc_type.__name__,
                    "line_number": exc_traceback.tb_lineno,
                    "exception": traceback.format_exception(exc_type, exc_value, exc_traceback),
                    "stack_trace": traceback.format_stack(),
                }
            }
            data["error"] = {**exc_info}

        return json.dumps(data, sort_keys=True)

    def _to_iso8601(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).isoformat(timespec="seconds") + "Z"


def setup_logger():
    # get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # remove any handlers that may have been added by dependent packages
    if root_logger.handlers:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(JsonFormatter())

    # Add Handler to root logger
    root_logger.addHandler(console_handler)

    logging.getLogger("botocore").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)