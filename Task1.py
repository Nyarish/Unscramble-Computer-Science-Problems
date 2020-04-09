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
# create a set()
uniques_numbers = set()

for i in range(len(texts)):
    # Find uniques phone numbers for both sender and reciver in texts.
    uniques_numbers.add(texts[i][0])
    uniques_numbers.add(texts[i][1])

for v in range(len(calls)):
    # Find uniques phone numbers for both sender and reciver in texts.
    uniques_numbers.add(calls[v][0])
    uniques_numbers.add(calls[v][1])

print("There are {} different telephone numbers in the records.".format(len(uniques_numbers)))

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
