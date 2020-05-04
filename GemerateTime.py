# import datetime
#
# x = datetime.datetime(2018, 9, 15)
#
# print(x.strftime("%b %d %Y %H:%M"))

from datetime import timedelta, date,datetime

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

start_dt = date(2019, 12, 1)
end_dt = date(2020, 1, 1)
for dt in daterange(start_dt, end_dt):
       print(dt.strftime("%d"'th '"%B %y"))
       now = datetime.now()
       print(now.strftime(" %X"))


