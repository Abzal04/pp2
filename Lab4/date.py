############# ex 1
from datetime import datetime, timedelta
dt=datetime.today()-timedelta(hours=4)
print(dt)

############# ex 2
from datetime import datetime, timedelta
todays_day=datetime.today()
yesterday=datetime.today()-timedelta(days=1)
tomorrow=datetime.today()+timedelta(days=1)
print(yesterday.strftime("%d"))
print(todays_day.strftime("%d"))
print(tomorrow.strftime("%d"))


############# ex 3
import datetime

def drop(ms):
    return ms.replace(microsecond=0)

current_time=datetime.datetime.now()
without_ms=drop(current_time)
print(without_ms)

############# ex4
import datetime
fdate=datetime.today()
sdate=datetime(2023,1,23)
diff=fdate-sdate
print(diff)
