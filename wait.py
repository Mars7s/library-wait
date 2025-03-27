import time # This is the library itself
def wait_secound():
    time.sleep(1)
def wait_minute():
    time.sleep(60)
def wait_hour():
    time.sleep(3600)
def wait_day():
    time.sleep(86400)
def wait_secound_2(secound):
    time.sleep(secound)
def wait_minute_2(minute):
    a = minute * 60
    time.sleep(a)
def wait_hour_2(hour):
    a = hour * 60 * 60
    time.sleep(a)
def wait_day_2(day):
    a = minute * 60 * 60 * 60
    time.sleep(a)
