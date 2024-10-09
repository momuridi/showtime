from datetime import datetime
import pytz
from os import getenv

def get_time(timezone) -> str:
    time_format = "%d.%m.%Y %H:%M"
    return datetime.now(timezone).strftime(time_format)

def environment_time_now():
    TIMECONF = pytz.timezone(getenv('TIME_ENV', local_timezone()))
    return get_time(TIMECONF)

def local_timezone() -> str:
    utc_now = datetime.now(pytz.utc)
    local_now = utc_now.astimezone()
    return local_now.tzname()