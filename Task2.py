"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def update(num, time, length):
    if num not in time:
        time[num] = length
    else:
        time[num] += length

time = {}
for num1, num2, _, length in calls:
    length = int(length)
    update(num1, time, length)
    update(num2, time, length)

longest = 0
longest_num = None

for num in time.keys():
    if time[num] > longest:
        longest = time[num]
        longest_num = num

if longest_num:
    print('{0} spent the longest time, {1} seconds, on the phone during September 2016.'.format(longest_num, longest))
