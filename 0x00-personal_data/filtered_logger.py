#!/usr/bin/env python3
""" Obfuscated personal data, done by filter_datum"""
import re
import logging
from typing import List
import os
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Obfuscated personal data is obtained from this function"""
    combo = "(?<=" + f"=)[^{separator}]*|(?<=" \
            .join(fields) + f"=)[^{separator}]*"
    return(re.sub(combo, '{}'.format(redaction), message))


def get_logger() -> logging.Logger:
    """ Creates a logger """
    user_data = logging.getLogger('user_data')
    user_data.propagate = False
    user_data.setLevel(level=logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    # Attaching our custom formatter to the stream handler
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(stream_handler)
    return(user_data)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Creates a database connection """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(user=username,
                                   password=password,
                                   host=host,
                                   database=database,
                                   auth_plugin='mysql_native_password')

    return conn


def main():
    # Getting the logger
    logger = get_logger()
    # Getting the connection object
    con = get_db()
    cursor = con.cursor()
    query = ("SELECT * FROM users")
    cursor.execute(query)
    for item in cursor:
        logger.info('name={}; email={}; phone={}; ssn={}; password={};'
                    'ip={}; last_login={}; user_agent={};'.
                    format(item[0], item[1], item[2], item[3],
                           item[4], item[5], item[6], item[7]))


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


if __name__ == '__main__':
    main()
