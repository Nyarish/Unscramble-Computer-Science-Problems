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


def getAreaCodes(calls):

    Bangalore_nums = set() # O(1)
    for num in calls: # O(n)
        # check if caller and reciver is from bangalore
        if num[0].startswith("(080)"):
            if num[1].startswith('('):
                fixed_prefix = num[1].split(")")
                Bangalore_nums.add(fixed_prefix[0])#add(num[1])
            if num[1].startswith('7'):
                Bangalore_nums.add(num[1][:4])
            if num[1].startswith('8'):
                Bangalore_nums.add(num[1][:4])
            if num[1].startswith('9'):
                Bangalore_nums.add(num[1][:4])
            if num[1].startswith('140'):
                Bangalore_nums.add(num[1])
    Bangalore_records = list(Bangalore_nums) #O(1)
    Bangalore_records.sort() # O(n log n)
    return Bangalore_records

Bangalore_records = getAreaCodes(calls)

print("The numbers called by people in Bangalore have codes:")
for area_code in Bangalore_records:
    print(area_code)


def getPercentageOfCalls(calls):
    counter_1 = 0
    counter_2 = 0

    for call in calls: # O(n)
        if call[0].startswith("(080)"):
            counter_1 += 1  #denominator - all the calls from (080)
            if call[1].startswith("(080)"):
                counter_2 += 1.  #numerator - all the calls from (080) to (080)

    percentage = round((counter_2 / counter_1)*100,2)
    return percentage

percentage = getPercentageOfCalls(calls)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
