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

dialed_num = []
for i in range(len(calls)):
  # Removing the generalization from the code and checking additional 
  # conditions below is the suggested algorith during the review
  # for every_record in calls:
  # if record[0] starts with (080):
      #if record[1] starts with '(0' then add what is between '(' and ')' to the container. 
      #if record[1] starts with '140' then add '140' to the container.
      #if record[1] starts with 7, 8, or 9 then add the first four digits of record[1] to the container.
    if calls[i][0][:5] == '(080)':
        if calls[i][1][0] == '(':
            find_closed_brackets = calls[i][1].find(')')
           #if record[1] starts with '140' then add '140' to the empty list 
            dialed_num.append(calls[i][1][:find_closed_brackets+1])
        elif calls[i][1][:3] == '140':

            dialed_num.append('140')
        else:
            dialed_num.append(calls[i][1][:4])

# We need this to calculate percent
get_total_dialed_num= len(dialed_num)

# count the total number of 
count = dialed_num.count('(080)')
# get the distincs dailed_num
dialed_num = sorted(set(dialed_num))
print("The numbers called by people in Bangalore have codes:")
for code in dialed_num:
    print(code)

# Part B

pct = count * 100 / get_total_dialed_num
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(pct, 2)))

# in below we will check if the number has closed bracket
# check if it has open  and closed brackets
# replace all the ocurrences with zero space charcater


