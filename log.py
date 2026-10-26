import os
import datetime
import pandas as pd
import socket


id = socket.gethostname()
try:
    user = os.getlogin()
except OSError:
    user = os.environ.get('USERNAME', 'unknown')


def now_time():
    date = datetime.datetime.now().strftime('%d.%m.%Y')
    return date


def sec():
    now_datetime = str(datetime.datetime.now()).split()
    time = now_datetime[1]
    return time


def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        data = {
            'id': [id],
            'pc_username': [user],
            'function_name': [func.__name__],
            'date': [now_time()],
            'time': [sec()]
        }
        df = pd.DataFrame(data)

        if os.path.isfile('log.csv'):
            df.to_csv('log.csv', mode='a', index=False, header=False)
        else:
            df.to_csv('log.csv', index=False)

        return res
    return wrapper