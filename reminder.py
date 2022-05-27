# Simple Python reminder app
# By https://hackernoon.com/a-simple-python-reminder-app-m3k42wk

import time
print("What shall I remind you about?")
text = str(input())
print("In how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)
