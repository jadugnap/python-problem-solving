"""
Read file into texts and calls.
It's ok if you don't understand how to read files

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_duration = 0
max_duration_number = ""
duration_dict = dict()

for call_record in calls:
    # calculate callers duration = new + existing duration
    total_duration = int(call_record[3]) + duration_dict.get(call_record[0], 0)
    duration_dict[call_record[0]] = total_duration
    if max_duration < total_duration:
        max_duration_number = call_record[0]
        max_duration = total_duration
    
    # calculate receivers duration = new + existing duration
    total_duration = int(call_record[3]) + duration_dict.get(call_record[1], 0)
    duration_dict[call_record[1]] = total_duration
    if max_duration < total_duration:
        max_duration_number = call_record[1]
        max_duration = total_duration

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_duration_number, max_duration))
