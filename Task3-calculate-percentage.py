"""
Read file into texts and calls.
It's ok if you don't understand how to read files.

text.csv columns: sending number (string), receiving number (string), message timestamp (string).
call.csv columns: calling number (string), receiving number (string), start timestamp (string), duration in seconds (string)
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
"""
"""
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
"""

def get_code(number):
    """
    Get area code (0xx)/(140) or mobile prefix (xxxx) from a given telephone number.
    
    Arguments:
        number (string)
    Returns:
        area code / mobile prefix (string)
    """
    if number[0] == '(':
        last_index = number.find(')')
        return number[:last_index+1]
    elif number[:3] == "140":
        return "140"
    else:
        return number[:4]

# get all codes receiving calls from Bangalore
receiver_codes = [get_code(c[1]) for c in calls if get_code(c[0]) == "(080)"]
print("The numbers called by people in Bangalore have codes:")
print("\n".join(sorted(set(receiver_codes))))

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangalore_count = sum([1 for code in receiver_codes if code == "(080)"])
percentage = "{:.2f}".format(100.0 * bangalore_count / len(receiver_codes))
print("{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
