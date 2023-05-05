#!/usr/bin/env python3
"""filtered logger"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function to filter data"""
    for field in fields:
        newMessage = re.sub("(?<={}=)(.*?)(?={})".format(field, separator),
                            redaction, message)
        message = newMessage
    return newMessage
