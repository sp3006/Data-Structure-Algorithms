
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
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

# create empty dictionry to collect the output
d = {}
# iterate throught the calls to get first two columns from 
# csv files which has phone number 
for call in calls:
    # loop in csv file for first two columns which are our telephone number
    for i, phone in enumerate(call[:2]):
        # print(call[:2]) 
        # in below we areusing the get method  
        # where we observe if there is not phone it will put the ith index
        # as default value
        # .get(<key>) searches dictionary d for <key> and returns the associated value if it is found. 
        # If <key> is not found, it returns None
        print("This is " , d.get(phone, i))
        d[phone] = d.get(phone, i) + int(call[3])
        print(d[phone])
longest_call_duration = max(d.items(), key=operator.itemgetter(i))

print(longest_call_duration[0], 'spent the longest time,', longest_call_duration[1],
      'seconds, on the phone during September 2016.')