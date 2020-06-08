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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers_set = set()
for text_record in texts:
    # count senders
    numbers_set.add(text_record[0])
    # count receivers
    numbers_set.add(text_record[1])
for call_record in calls:
    # count callers
    numbers_set.add(call_record[0])
    # count receivers
    numbers_set.add(call_record[1])
print("There are {0} different telephone numbers in the records.".format(len(numbers_set)))
