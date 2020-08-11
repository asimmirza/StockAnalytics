import pytz
from datetime import datetime, timedelta
from pytz import timezone

class TimeIndia:
    def getCurrentTime():
        time_india = pytz.timezone("Asia/Calcutta")
        act_time = datetime.now(time_india)
        return act_time


