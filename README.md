# python-problem-solving
A basic problem solving in data analysis with Python.



## Usage

- `python3 Task0-single-record.py`
- ...
- `python3 Task4-predict-telemarketers.py`



## Time Complexity Analysis

### Task 0 - first record and last record
- O(1) `sender, receiver, time = texts[0][0], texts[0][1], texts[0][2]`
- O(1) `caller, receiver, start, duration = calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]`

Worst-case complexity: O(1) + O(1) = O(1)
#### Task 0 Complexity: O(1)


### Task 1 - unique records
O(n) `for text_record in texts:`
- O(1) `numbers_set.add`

O(n) `for call_record in calls:`
- O(1) `numbers_set.add`

Worst-case complexity: O(n) x O(1) + O(n) x O(1) = O(2n) = O(n)
####  Task 1 Complexity: O(n)


### Task 2 - duration calculation
O(n) `for call_record in calls:`
- O(1) `total_duration = ...`
- O(1) `duration_dict[...] = total_duration`
O(n) `max_on_call = max(duration_dict.items(), key=lambda x: x[1])`

Worst-case complexity: O(2n) + O(n) = O(3n) = O(n)
####  Task 2 Complexity: O(n)


### Task 3 - percentage calculation

O(4n) `receiver_codes = [get_code(c[1]) for c in calls if get_code(c[0]) == "(080)"]`
- O(n) `for c in calls`
- O(4) `def get_code(number):`

O(n log(n)) `sorted(set(receiver_codes))`

O(n) `bangalore_count = sum([1 for code in receiver_codes if code == "(080)"])`
- O(n) `for code in receiver_codes`
- O(1) `sum(list_len_n)`

O(1) `percentage = "{:.2f}".format(100.0 * bangalore_count / len(receivers))`

Worst-case complexity: O(4n) + O(n log(n)) + O(n) + O(1) = O(n log(n))
####  Task 3 Complexity: O(n log(n))


### Task 4 - telemarketers prediction
- O(n) `text_senders = set([t[0] for t in texts])`
- O(n) `text_receivers = set([t[1] for t in texts])`
- O(n) `call_receivers = set([c[1] for c in calls])`
- O(n) `whitelist = call_receivers.union(text_senders, text_receivers)`

O(n log(n)) `callers = sorted(set([c[0] for c in calls if c[0] not in whitelist]))`

Worst-case complexity: O(4n) + O(n log(n)) = O(n log(n))
####  Task 4 Complexity: O(n log(n))
