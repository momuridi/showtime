from datetime import datetime
import pytz
from os import getenv

# Get current time in specified timezone
def format_timenow(tz) -> str:
    time_format = "%d.%m.%Y %H:%M"
    return datetime.now(tz).strftime(time_format)

# Get current time in environment timezone
def environment_time_now():
    tz = getenv('TIME_ENV')
    if tz:
        TIMECONF = pytz.timezone(tz)
    else:
        TIMECONF = None
    return format_timenow(TIMECONF)
    