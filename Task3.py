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
# PART A
# the below get_numbers iterate thru the calls and checks if the 
# call has '(080)' in the string
# the get_numbers_for_banglore has number which has "(080)" which is 
# banglore area code
# Another approach for the same use case is to  
# first declare the empty list variable to collect the output form the
# for loops in two stages with if coditions however we are using
# list comprehension in below implementations
get_numbers_called_by_banglore_population = [call[1] for call in calls if call[0][:5] == '(080)']
# in below we will check if the number has closed bracket
# check if it has open  and closed brackets
# replace all the ocurrences with zero space charcater
fetch_std_codes = [phone[:phone.find(')') + 1].replace('(', '').replace(')', '') if ')' in phone else phone[0:4] for phone in
              get_numbers_called_by_banglore_population]
print('The numbers called by people in Bangalore have codes:\n' + '\n'.join(sorted(set(fetch_std_codes))))

# PART B
print()
print('{0:.2f}'.format(
    (len([phone for phone in get_numbers_called_by_banglore_population if '(080)' in phone]) / len(get_numbers_called_by_banglore_population)) * 100),
    'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')