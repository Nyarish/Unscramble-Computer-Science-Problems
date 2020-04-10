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


def getLongestTime(calls):

    phone_record_dict = {} # O(1)

    for caller, reciver, time_stamp, duration in calls: # O(n) for the loop
        if caller not in phone_record_dict:
            phone_record_dict[caller] = int(duration)
        else:
            phone_record_dict[caller] += int(duration)
        if reciver not in phone_record_dict:
            phone_record_dict[reciver] = int(duration)
        else:
            phone_record_dict[reciver] += int(duration)

    phone, time = (max(phone_record_dict.items(), key=lambda x: x[1])) # O(n)
    return phone, time

phone_number, call_duration = getLongestTime(calls)
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(phone_number, call_duration))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
