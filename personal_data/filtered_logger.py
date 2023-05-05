#!/usr/bin/env python3
"""filtered logger"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function to filter data"""
    for field in fields:
        newMessage = re.sub("(?<={:s}=)(.*?)(?={:s})".format(field, separator),
                            redaction, message)
    return newMessage
