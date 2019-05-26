from datetime import datetime
from datetime import timezone
from mock import patch
import pytest
import pytz

from patch_reporter.datetime_utils import calculate_date_difference
from patch_reporter.datetime_utils import parse_date
import patch_reporter


MELBOURNE_TIMEZONE = 'Australia/Melbourne'
PATTERNS = ['%Y%m%d']


def test_parse_date_validate_input_string():

    with pytest.raises(ValueError):
        parse_date(
            date="10312015",
            patterns=PATTERNS,
            tzinfo=MELBOURNE_TIMEZONE
        )
    with pytest.raises(ValueError):
        parse_date(
            date="31102015",
            patterns=PATTERNS,
            tzinfo=MELBOURNE_TIMEZONE
        )


def test_parse_date_correctness_tz_is_utc():

    dt = parse_date(
            date='20190518',
            patterns=PATTERNS,
            tzinfo='utc'
        )
    assert dt == datetime(2019, 5, 18, tzinfo=timezone.utc)


def test_parse_date_correctness_tz_not_utc():

    dt = parse_date(
            date='20190518',
            patterns=PATTERNS,
            tzinfo=MELBOURNE_TIMEZONE
        )
    assert dt == datetime(2019, 5, 18, tzinfo=pytz.timezone(MELBOURNE_TIMEZONE))


@patch(
        'patch_reporter.datetime_utils.get_utc_now',
        return_value=datetime(2019, 5, 18, 23, 55, 0, tzinfo=timezone.utc)
    )
def test_calculate_date_difference(self):

    dt = datetime(2019, 5, 15, tzinfo=timezone.utc)
    assert calculate_date_difference(dt) == 3

    dt = datetime(2019, 5, 15, tzinfo=pytz.timezone(MELBOURNE_TIMEZONE))
    assert calculate_date_difference(dt) == 4

    dt = datetime(2019, 5, 15, 12, 31, 59, tzinfo=pytz.timezone(MELBOURNE_TIMEZONE))
    assert calculate_date_difference(dt) == 3