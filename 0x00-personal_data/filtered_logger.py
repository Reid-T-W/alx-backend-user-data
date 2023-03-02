#!/usr/bin/env python3
""" Obfuscated personal data """
import re


def filter_datum(fields, redaction, message, separator):
    """ Obfuscated personal data """
    combo = "(?<=" + f"=)[^{separator}]*|(?<=" \
            .join(fields) + f"=)[^{separator}]*"
    return(re.sub(combo, '{}'.format(redaction), message))
