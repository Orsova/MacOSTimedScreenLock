from ctypes import CDLL
import datetime
import time

def time_in_range(start, end, current):
    return start <= current <= end

# set first times for before midnight, second times for after midnight.

start = datetime.time(22, 30, 0)
end = datetime.time(23, 59, 59)

start2 = datetime.time(0, 0, 0)
end2 = datetime.time(7, 0, 0)

while True:

    current = datetime.datetime.now().time()

    if time_in_range(start, end, current):
        # print (current)
        # print(bool(time_in_range(start, end, current)))
        loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        result = loginPF.SACLockScreenImmediate()
        time.sleep(15)
    elif time_in_range(start2, end2, current):
        # print(current)
        # print(bool(time_in_range(start2, end2, current)))
        loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
        result = loginPF.SACLockScreenImmediate()
        time.sleep(15)
    else:
        # print (current)
        # print(bool(time_in_range(start, end, current)))
        time.sleep(5)
