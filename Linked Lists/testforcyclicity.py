# Can create a cyclic linked list by making the next
# field of an element reference an earlier node.
# Write a program that takes the head of a singly linked list
# and returns null if there does not exist a cycle,
# but return the node at the start of the cycle if one is present.

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

def delete_after(node):
    node.next = node.next.next

def printNode(node):
    temp = node
    print(temp.data)
    while temp.next:
        temp = temp.next
        print(temp.data)


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


# attempt
def testCycle(L):
    slower = faster = L
    while faster is not None:
        for _ in range(2):
            if faster.next:
                faster = faster.next
            else:
                return None
        slower = slower.next
        if faster == slower:
            return L
    return None

#printNode(a)
#print(testCycle(a))

# Book says a brute-force approach with O(1) storage and no
# list modification can traverse the list in two loops.
# Outer loop traverses nodes one by one and the inner loop
# goes through all the nodes that the outer loop goes through to compare
# and if the node being visited by the outer one is visited twice, 
# then it means there's a loop. O(n^2) time complexity.

# This can also be done in linear time using a slow iterator and
# a fast iterator. Advance slow by one and fast by two.
# List has a cycle if the two iterators meet. 
# 

# Can find the length of the cycle by advancing until
# the same node is hit. 

def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Find start of cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            
            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None
