# Complete the solution so that the function will break up camel casing, using a space between words.
# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""



# My Solution
def solution(s):
    new_s = ""
    for i in range(len(s)):
        if s[i].isupper():
            new_s += " " + s[i]
        else:
            new_s += s[i]
    list = new_s.split()
    return " ".join(list)

#Best Practice and Clever-1
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

#Best Practive and Clever-2
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)