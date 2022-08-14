# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"



# My Solution
def name_shuffler(str_):
    return str_[str_.find(" ") + 1:] + " " + str_[0: str_.find(" ")]