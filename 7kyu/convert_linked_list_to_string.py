# Preloaded

# Preloaded for you is a class, struct or derived data type Node ( depending on the language ) used to construct linked lists in this Kata:

# class Node():
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

# Prerequisites

# This Kata assumes that you are already familiar with the idea of a linked list. If you do not know what that is, you may want to read this article on Wikipedia. Specifically, the linked lists this Kata is referring to are singly linked lists, where the value of a specific node is stored in its data / $data / Data property, the reference to the next node is stored in its next / $next / Next / next_node property and the terminator for a list is null / NULL / None / nil / nullptr / null().
# Task

# Create a function stringify which accepts an argument list / $list and returns a string representation of the list. The string representation of the list starts with the value of the current Node, specified by its data / $data / Data property, followed by a whitespace character, an arrow and another whitespace character (" -> "), followed by the rest of the list. The end of the string representation of a list must always end with null / NULL / None / nil / nullptr / null() ( all caps or all lowercase depending on the language you are undertaking this Kata in ). For example, given the following list:

# Node(1, Node(2, Node(3)))

# ... its string representation would be:

# "1 -> 2 -> 3 -> None"

# And given the following linked list:

# Node(0, Node(1, Node(4, Node(9, Node(16)))))

# ... its string representation would be:

# "0 -> 1 -> 4 -> 9 -> 16 -> None"


# My Solution
def stringify(node):
    string = ""
    current = node
    while current is not None:
        string += str(current.data) + " -> "
        current = current.next
    if current is None:
        string += "None"
    return string