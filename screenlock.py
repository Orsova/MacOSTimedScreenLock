from ctypes import CDLL
import datetime
import time

def time_in_range(start, end, current):
    return start <= current <= end

start = datetime.time(20, 0, 0)
end = datetime.time(7, 0, 0)

while True:

    current = datetime.datetime.now().time()

    if time_in_range(start, end, current):
        # print (current)
        # print(bool(time_in_range(start, end, current)))
        loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        result = loginPF.SACLockScreenImmediate()
        time.sleep(5)
    else:
        # print (current)
        # print(bool(time_in_range(start, end, current)))
        time.sleep(5)
