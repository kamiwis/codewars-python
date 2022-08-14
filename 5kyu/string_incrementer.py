# Your job is to write a function which increments a string, to create a new string.

#     If the string already ends with a number, the number should be incremented by 1.
#     If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.


# My Solution
import re
def increment_string(strng):
    m = re.search(r'\d*$', strng)
    num_str = m.group()
    length_num = len(num_str)
    if length_num == 0:
        return strng + "1"
    elif length_num > 0:
        non_num_str = strng[0: strng.find(num_str)]
        number = int(num_str) + 1
        incremented_num_str = str(number)
        return non_num_str + incremented_num_str.zfill(length_num)

#Best Practice
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

