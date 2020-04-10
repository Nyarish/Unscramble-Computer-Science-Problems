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


def getUniqueNumbers(calls, texts):
    # create a set()
    # Time Complexity is O(1)
    uniques_numbers = set()

    # Time Complexity is O(n)
    for i in range(len(texts)):
        # Find uniques phone numbers for both sender and reciver in texts.
        uniques_numbers.add(texts[i][0])
        uniques_numbers.add(texts[i][1])
    # Time Complexity is O(n)
    for v in range(len(calls)):
        # Find uniques phone numbers for both sender and reciver in texts.
        uniques_numbers.add(calls[v][0])
        uniques_numbers.add(calls[v][1])

    return list(uniques_numbers)

phone_numbers = getUniqueNumbers(calls, texts)

print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
