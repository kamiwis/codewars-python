# Description:

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# My Solution
def is_pangram(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    list = []
    for i in range(len(abc)):
        list.append(s.lower().count(abc[i]))
    return False if 0 in list else True

# Best Practices 
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
        