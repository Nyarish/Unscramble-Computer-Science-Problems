"""
Task0.py
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
# Create variables to store the numbers, timestamp and duration fot text and calls

# texts
text_sender_number = texts[0][:1]
text_reciver_number = texts[0][1:-1]
text_time_stamp = texts[0][2:]

# calls 
calls_sender_number = calls[-1][:1]
calls_reciver_number = calls[-1][1:-2]
call_time_stamp = calls[-1][2:3]
call_duration = calls[-1][-1]

print("First record of texts, {} texts {} at time {}".format(text_sender_number[0], text_reciver_number[0], text_time_stamp[0]))


print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls_sender_number[0], calls_reciver_number[0], call_time_stamp[0], call_duration[0]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
