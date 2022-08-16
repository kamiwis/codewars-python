# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


# My Solution
def descending_order(num):
    num_str = str(num)
    num_list = []
    for n in num_str:
        num_list.append(n)
    num_list.sort()
    num_list.reverse()
    return int("".join(num_list))

#Best Practice
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
    