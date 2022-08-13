# Instructions

# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
# Example

# Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );


# My Solution
def capitals(word):
    return sorted([i for i in range(len(word)) if word[i].isupper()])

# Best Practice
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]