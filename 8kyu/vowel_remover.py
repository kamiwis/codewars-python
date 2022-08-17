# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
# Examples

# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"

#     don't worry about uppercase vowels
#     y is not considered a vowel for this kata



# My Solution
def shortcut(s):
    new_str = ""
    for letter in s:
        if letter in "aeiou":
            continue
        else:
            new_str += letter
    return new_str

# Best Practice
def shortcut(s):
    return s.translate(None, 'aeiou')