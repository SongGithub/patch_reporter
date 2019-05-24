
# -*- coding: utf-8 -*-

"""
patch-reporter - utils
~~~~~~~~~~~~~~
This module provides utility functions
that are also useful for external consumption.
"""

from datetime import datetime
import pytz

# TO BE MOVED TO STANDALONE CONFIG FILE

# time zone info for input date string
INPUT_TIME_ZONE = 'Australia/Melbourne'
# alternative setting:
# INPUT_TIME_ZONE = 'UTC'

PATTERNS = ['%Y%m%d']


def parse_date(date:str,patterns,tzinfo=None) -> datetime:
    for pattern in patterns:
        try:
            return datetime.strptime(date, pattern).replace(tzinfo=pytz.timezone(tzinfo))
        except ValueError:
            pass
    raise ValueError(
        f'date value "{date}" does not match any of PATTERN settings')


def calculate_date_difference(input_time) -> int:
    '''check date difference between current date(UTC) and input date(UTC)'''

    # using 'replace' to add in offset-awareness property to have the following
    # date diff calculation to run correctly
    utc_now = datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'))
    print("current UTC time is ", utc_now)
    return (utc_now - input_time).days


if __name__ == 'main':
    dt = parse_date(date='20190518',patterns=PATTERNS,tzinfo=INPUT_TIME_ZONE)
    print(calculate_date_difference(dt))
