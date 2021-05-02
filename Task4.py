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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# using dictionary collecion we will get the numbers making outgoing calls
# in our given texts csv file the 1 st column is for sender of text
# which is represeted with texts[:2]
get_senders_num_list = {phone for text in texts for phone in text[:2]}
get_caller_receivers_num_list = {call[1] for call in calls}
get_markts_outgoing = {call[0] for call in calls if call[0] not in get_senders_num_list and call[0] not in get_caller_receivers_num_list}
# for our final goal we will only take those number where
# receivers are not present as sender and sender in present as
# one entity or number which only or distinct sender number 
# for eg sushant (calls) Raj here sushant is sender however if
# sushant is getting call from Raj then sushant's number is not considered
# as "outgoing only number"
print('These numbers could be telemarketers:')
print('\n'.join(sorted(get_markts_outgoing)))
# print(' Total outgoing margeting calls ', len(get_markts_outgoing))
    
# Time analysis
# 
# Our above code with dictionay access is simple array data structure access and according to 
# https://www.bigocheatsheet.com/ & udacity lesson explain Big(O) we observe below
# The get_senders_num_list has, get_caller_receivers_num_list and get_markts_outgoing 
# O(n) time complexity which can be represented as O(3n)
# The call using sorted function sorted(get_markts_outgoing) O(nlogn) complexity
# O(3n) + O(nlogn) --> O(3n + nlog(n) ) --> Θ(n log(n))
 