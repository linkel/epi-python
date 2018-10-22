# Singly linked list is a data structure that contains a sequence
# of nodes such that each node contains an obj and a reference to the
# next node in the list. 

# First node is the head. Last node is the tail. Tail has null as next field.
# There are variants. Doubly linked list holds an obj and two references,
# to the previous and to the next.

# This is the prototype of a node:

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

# Book asserts that there are two types of list problems.
# One is where you hae to implement your own list. 
# the next is where you have to exploit the standard list library. 

# Generally a list API will have search, insert, and delete capabilities.

def search_list(L, key):
    while L and L.data != key:
        L = L.next
        # if key not present in the list then L will be null
    return L

def insert_after(node, new_node):
    # insert new node after the specified node
    # the original next node is saved to the new node's next node
    # the next node to the original node becomes the new
    # this order is important so that you don't lose node.next
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    # skip over the node by replacing the next node with the next next node
    node.next = node.next.next

# time complexity is O(1) for insert and delete as written above
# but for search it takes O(n) where n is # of nodes

# List problems frequently have a brute force solution that uses O(n) space
# There may be solutions that use the existing nodes to simplify to O(1) space
# Dummy heads (or sentinels) allow avoidance of needing to check for empty list.
# Don't forget to update the next for the head and tail!
# algos on singly linked lists can benefit from using two iterators,
# one ahead or one advancing quicker than the other.

# Python's list type is usually implemented as a dynamically resized array.
# Linked lists are not a standard type in Python.