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

"""
The text data (text.csv) has the following columns: 
sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
so first two columns are telephone numbers
The call data (call.csv) has the following columns: 
calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), 
duration of telephone call in seconds (string)
first two columns are pone numbers

"""

telephone_numbers = set()
for i in range(len(texts)):
    # appending the dictionary with unique records
    telephone_numbers.add(texts[i][0])
    telephone_numbers.add(texts[i][1])
for i in range(len(calls)):
    telephone_numbers.add(calls[i][0])
    telephone_numbers.add(calls[i][1])

print("There are {} different telephone numbers in the records.".format(
    len(telephone_numbers)))