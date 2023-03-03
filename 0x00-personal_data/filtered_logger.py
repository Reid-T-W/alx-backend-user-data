#!/usr/bin/env python3
""" Obfuscated personal data, done by filter_datum"""
import re
import logging


def filter_datum(fields: str, redaction: str, message: str,
                 separator: str) -> str:
    """ Obfuscated personal data is obtained from this function"""
    combo = "(?<=" + f"=)[^{separator}]*|(?<=" \
            .join(fields) + f"=)[^{separator}]*"
    return(re.sub(combo, '{}'.format(redaction), message))


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ Initialization method for RedactingFormatter """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Hides personal data before logging """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super(RedactingFormatter, self).format(record))
