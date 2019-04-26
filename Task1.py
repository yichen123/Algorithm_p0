"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

met = []
count = 0
for entry in calls:
    num1, num2 = entry[0], entry[1]
    if num1 not in met:
        met.append(num1)
        count += 1
    if num2 not in met:
        met.append(num2)
        count += 1

for entry in texts:
    num1, num2 = entry[0], entry[1]
    if num1 not in met:
        met.append(num1)
        count += 1
    if num2 not in met:
        met.append(num2)
        count += 1

print("There are {0} different telephone numbers in the records.".format(count))
