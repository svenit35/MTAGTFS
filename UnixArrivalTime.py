from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo
import math

def time_until_arrival(arrivaltime_unix):
    current_unix_time = round(datetime.now().timestamp())

    time_left = arrivaltime_unix - current_unix_time
    if time_left < 0:
        return 0
    else:
        return time_left // 60
