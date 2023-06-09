#!/usr/bin/env python3
"""filtered logger"""
import re
from typing import List
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'email')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function to filter data"""
    for field in fields:
        newMessage = re.sub("(?<={}=)(.*?)(?={})".format(field, separator),
                            redaction, message)
        message = newMessage
    return newMessage


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Init Redacting Formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the class object"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''Returns a logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    logger.setFormatter(RedactingFormatter(PII_FIELDS))
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database PERSONAL_DATA_DB_NAME """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=user, password=password,
                                   host=host, database=database)


def main():
    """ main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]
    logger = get_logger()
    for row in cursor:
        message = ""
        for i in range(len(fields)):
            message += f"{fields[i]}={row[i]};"
        logger.info(message)
    cursor.close()
    db.close()
