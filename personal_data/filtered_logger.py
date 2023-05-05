#!/usr/bin/env python3
"""filtered logger"""
import re


def filter_datum(fields, redaction, message, separator):
    """Function to filter data"""
    for field in fields:
        newMessage = re.sub("(?<={:s}=)(.*?)(?={:s})".format(field, separator),
                            redaction, message)
    return newMessage
