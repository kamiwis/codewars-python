# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples

#     "foefet" is an anagram of "toffee"

#     "Buckethead" is an anagram of "DeathCubeK"


# My Solution
def is_anagram(test, original):
    for letter in test.lower():
        if test.lower().count(letter) != original.lower().count(letter):
            return False
    for letter in original.lower():
        if test.lower().count(letter) != original.lower().count(letter):
            return False
    return True

# Best Practice
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 