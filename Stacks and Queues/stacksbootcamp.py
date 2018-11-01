# Stacks! Last in first out. Like dinner trays in a cafeteria.
# Book says they're useful for creating reverse iterators for sequences
# that are stored in a way that would make it difficult or impossible
# to step back from a given element. 

# Here's a program that uses a stack to print the entries of a singly
# linked list in reverse order.

def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())

# Time and space complexity are O(n) where n is # of nodes in the list.
# Can also perform reverse of the list using Problem 7.2
# then iterate through list to print entries
# and perform another reverse, which would have O(n) time and
# O(1) space.

# Parsing usually benefits from a stack.
# can augment basic stack data structure to support more
# operations, like finding a max element.


