#!/usr/bin/env python3
""" Obfuscated personal data, done by filter_datum"""
import re
import logging
from typing import List
PII_FIELDS = ("email", "phone", "ssn", "password", "ip")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Obfuscated personal data is obtained from this function"""
    combo = "(?<=" + f"=)[^{separator}]*|(?<=" \
            .join(fields) + f"=)[^{separator}]*"
    return(re.sub(combo, '{}'.format(redaction), message))


def get_logger() -> logging.Logger:
    """ Creates a logger """
    user_data = logging.getLogger('user_data')
    user_data.setLevel(level=logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    # Attaching our custom formatter to the stream handler
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(stream_handler)
    return(user_data)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialization method for RedactingFormatter """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Hides personal data before logging """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super(RedactingFormatter, self).format(record))
