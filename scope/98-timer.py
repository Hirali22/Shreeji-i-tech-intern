# Timer/Stopwatch closure** storing start time.
import time

def timer():
    start_time = time.time()
    def inner():
        return time.time() - start_time
    return inner

stopwatch = timer()
print(stopwatch())
time.sleep(2)
print(stopwatch())