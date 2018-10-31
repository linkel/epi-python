# Given two singly linked list, there could be list nodes that are common to both.
# (what is a flyweight pattern? canonical form?)
# Write a program that takes two cycle-free singly linked lists, and 
# determines if there is a node that is common to both lists.

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def connect(node, next_node):
    node.next = next_node

def delete_after(node):
    node.next = node.next.next

def printNode(node):
    if node != None:
        temp = node
        print(temp.data)
        while temp.next:
            temp = temp.next
            print(temp.data)
    else:
        print("None, sadly")


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
insert_after(a, b)
insert_after(b, c)
insert_after(c, d) 
insert_after(d, e) 
insert_after(e, f) 
insert_after(f, g)

h = ListNode(8)
i = ListNode(9)
j = ListNode(10)
insert_after(h, i)
insert_after(i, j)
connect(j, f)

# Brute-force approach: store one list's nodes in a hash table,
# iterate through the nodes of the other, testing each
# Takes O(n) time and O(n) space.
# Alternately we can use two nested loops, iterating through the first list
# then the other to search the second for the node in the first
# time becomes O(n^2) while saving space. 

def overlap(L1, L2):
    # simple code to find the length of a linked list
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    # get the lengths
    L1_len, L2_len = length(L1), length(L2)
    # we want L2 to be the longer one, so if L1 is longer
    # we swap 'em for the purposes of this program
    if L1_len > L2_len:
        L1, L2 = L2, L1 
    # for the difference between the two, let's travel along L2
    # because once linked lists connect, they won't be separating out
    # so the part where they overlap, if they do overlap
    # will have to be the same length
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    # while the node exists and they aren't the same, keep travelling
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 # None implies no overlap between L1 and L2
    # otherwise it returns the first node where they overlap

printNode(overlap(h, a))

# time complexity is O(n) and space is O(1)