import random
from datetime import datetime
from datetime import date
import random
import pickle

f = open("First_log.txt", "w")
# f.write()


def random_date():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    random_d=random_day.strftime("%d"'th '"%B %Y")
    return random_d


def file_log():
    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)
    for items in range(30):
        error_code = ['ERROR', 'WARNING', 'INFO', 'DEBUG', 'CRITICAL']
        n = random.randint(120, 130)
        # print(n)
        random_error = random.choice(error_code)
        # print(random_error)
        now = datetime.now()
        random_time = now.strftime(" %X")
        line = (str(random_error)+':'+str(n)+':'+str(random_date())+':'+str(random_time)+'\n')
        # pickle.dump(line, f)
        f.write('print something '+line+'\n')


f.close()


