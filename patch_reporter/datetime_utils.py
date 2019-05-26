
"""
patch-reporter - datetime_utils
~~~~~~~~~~~~~~
This module provides utility functions
that are also useful for external consumption.
"""

from datetime import datetime
import pytz

# TO BE MOVED TO STANDALONE CONFIG FILE
INPUT_TIME_ZONE = 'Australia/Melbourne'
PATTERNS = ['%Y%m%d']


def parse_date(date:str,patterns,tzinfo='utc') -> datetime:
    for pattern in patterns:
        try:
            return datetime.strptime(date, pattern).replace(tzinfo=pytz.timezone(tzinfo))
        except ValueError:
            pass
    raise ValueError(
        f'date value "{date}" does not match any of PATTERN settings')

def get_utc_now():
    return datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'))

def calculate_date_difference(input_time:datetime) -> int:
    '''check date difference between current date(UTC) and input date(UTC)'''

    # using 'replace' to add in offset-awareness property to have the following
    # date diff calculation to run correctly
    utc_now = get_utc_now()
    print("current UTC time is ", utc_now)
    return (utc_now - input_time).days
