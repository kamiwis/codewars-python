# Linked Lists - Sorted Insert

# Write a SortedInsert() function which inserts a node into the correct location of a pre-sorted linked list which is sorted in ascending order. SortedInsert takes the head of a linked list and data used to create a node as arguments. SortedInsert() should also return the head of the list.

# sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
# sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
# sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

# The push() and buildOneTwoThree() functions do not need to be redefined.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# My Solution

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    current = head
    if current.data > new_node.data:
        new_node.next = current
        head = new_node
        return head
    previous = current
    current = current.next
    while current:
        if previous.data < new_node.data and current.data > new_node.data:
            previous.next = new_node
            new_node.next = current
            break
        else:
            previous = current
            current = current.next
    if current is None:
        previous.next = new_node
    return head