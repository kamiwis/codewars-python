# Description:

# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

#     Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#     A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#     Every smiling face must have a smiling mouth that should be marked with either ) or D

# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# My Solution
def count_smileys(arr):
    return sum(map(lambda x: 1 if x in [":)", ":-)", ":~)", ":D", ":-D", ":~D", ";)", ";-)", ";~)", ";D", ";-D", ";~D"] else 0, arr))

# Best Practices-1
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

# Best Practices - 2
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count