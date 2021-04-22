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

get_length_for_calls = len(calls)
get_length_for_texts = len(texts)

merge_data_sets = set(zip(texts , calls))

print(merge_data_sets[0][0])
