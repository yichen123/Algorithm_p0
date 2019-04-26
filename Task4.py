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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



def lexSort(list):
    # quick sort
    if len(list) <= 1:
        return list
    p = list[0]
    less = [i for i in list[1:] if i < p]
    great = [i for i in list[1:] if i > p]
    return lexSort(less) + [p] + lexSort(great)


telemarketers = []
nums = {'call_out':[], 'call_in':[], 'text_out':[], 'text_in':[]}

for num1, num2, _, _ in calls:
    if num1 not in nums['call_out']:
        nums['call_out'].append(num1)
    if num2 not in nums['call_in']:
        nums['call_in'].append(num2)

for num1, num2, _ in texts:
    if num1 not in nums['text_out']:
        nums['text_out'].append(num1)
    if num2 not in nums['text_in']:
        nums['text_in'].append(num2)

for num in nums['call_out']:
    if num not in nums['call_in'] and num not in nums['text_in'] and num not in nums['text_out']:
        telemarketers.append(num)


sorted = lexSort(telemarketers)
print("These numbers could be telemarketers: ")
if sorted:
    for num in sorted:
        print(num)
