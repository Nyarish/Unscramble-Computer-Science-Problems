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
# create a dictionary
phone_dict = {}
# for phone in range(len(calls)):
#     if calls[phone][0] not in phone_dict.keys():
#         phone_dict[calls[phone][0]] = int(calls[phone][3])
#     else:
#         phone_dict[calls[phone][0]] += int(calls[phone][3])

for number in range(len(calls)):
    phone_dict[calls[number][0]] = phone_dict.get(int(calls[number][3]), 0) + 1


phone_numbers = len(phone_dict.keys())
print("There are {} different telephone numbers in the records.".format(phone_numbers))

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
