# Given two singly linked lists there may be list nodes common to both.
# These lists may also have cycles. Determine if there is a node 
# common to both lists, and then return the node that appears first when
# traversing the lists. If one node ends in ac ycle, the first cycle node
# encountered when traversing it may be different from the first cycle
# node encountered when traversing the second list. Can return either of the two.

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

def printOneNode(node):
    print(node.data)

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
connect(g, d)

h = ListNode(8)
i = ListNode(9)
j = ListNode(10)
insert_after(h, i)
insert_after(i, j)
connect(j, f)

# Hash table approach using O(n) time and space is simple, says the book.
# To improve space complexity, can study different cases. 
# If neither list is cyclic (problem 7.3) then can use 7.4 solution. 
# If one list is cyclic and the other isn't, they can't overlap.

# here's the has cycle code from before:

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
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None

# here's the non cycle overlapping code from before:

def overlap(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 

def overlapping_lists(L1, L2):
    # Store the start of the cycle if there is one
    root1, root2 = has_cycle(L1), has_cycle(L2)

    if not root1 and not root2:
        # both lists don't have cycles 
        return overlap(L1, L2)
    elif (root1 and not root2) or (not root1 and root2):
        # One list has a cycle, the other list does not
        return None # since this means they cannot overlap
    # both lists must have cycles if code makes it here
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break
    # L1 and L2 do not end in the same cycle if temp is not root1
    # as reminder, root1 is where the cycle starts for L1
    if temp is not root1:
        return None # cycles are disjoint
    
    # this distance function is only used for when a is in front of b
    # and will get to b eventually or else we'd get an attribute error
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    # L1 and L2 end in the same cycle, locate the overlapping node if
    # they first overlap before cycle starts.
    stem1_length, stem2_length = distance(L1, root1), distance(L2, root2)
    # like in prev problems we want stem2 to be the longer one
    # we swap 'em if stem1 is longer
    if stem1_length > stem2_length:
        L2, L1 = L1, L2
        root1, root2 = root2, root1
    # travel forward by however much one is longer than the other
    # so that they can meet
    for _ in range(abs(stem1_length - stem2_length)):
        L2 = L2.next
    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next
    
    # If L1 == L2 before reaching root1, it means the overlap first occurs
    # before the cycle starts; otherwise, the first overlapping node is not
    # unique, we can return any node on the cycle.
    return L1 if L1 is L2 else root1


# time complexity of this algo is O(n+m) where n and m are the lengths
# of the input lists, and space complexity O(1)

printOneNode(overlapping_lists(a,h))