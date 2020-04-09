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



#Create a dictionary for sender phone calls records
callers_record = {}

for call in calls:
    for number in [0,1]:
        try:
            callers_record[call[number]] += int(call[3])
        except KeyError:
            callers_record[call[number]] = int(call[3])

print(len(callers_record.keys()))

# Loop the dictionary to get the number and call duration
max_call_time = 0
phone_number = " "

for record in callers_record:
    if callers_record[record] >= max_call_time:
        max_call_time = callers_record[record]
        phone_number = record

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(phone_number, max_call_time))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
