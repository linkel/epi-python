# Given a node in a singly linked list, deleting it in O(1) time 
# can be done if the node to delete is not the last one in the list,
# and if copying the value part of a node is simple. 

# Write a program which deletes a node in a singly linked list. The input
# node is guaranteed not to be the tail node.

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def insert_after(node, next_node):
    next_node.next = node.next
    node.next = next_node

def connect(node, next_node):
    node.next = next_node

def print_nodes(node):
    temp = node
    print(temp.data)
    while temp.next:
        temp = temp.next
        print(temp.data)

d = ListNode(4)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

print_nodes(a)

def kill_node(node):
    node.data = node.next.data
    node.next = node.next.next

# book says given the pointer to a node, you can't delete it without
# modifying the predecessor's next pointer and the only way to get
# to the predecessor is by traversing the list from head, which takes O(n)
# time. 

# but if you get a node, you can delete its successor easy since you just update
# the current node's next pointer. So if you copy the value of the next node
# to the current node and then delete the next node, you've effectively
# deleted the current node. This is why for this implementation you can't
# delete the last node. This takes O(1) time. 