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
text_senders = set([t[0] for t in texts])
text_receivers = set([t[1] for t in texts])
call_receivers = set([c[1] for c in calls])
whitelist = call_receivers.union(text_senders, text_receivers)
# print("\n".join(sorted(whitelist)))
callers = sorted(set([c[0] for c in calls if c[0] not in whitelist]))

print("These numbers could be telemarketers: ")
print("\n".join(callers))
