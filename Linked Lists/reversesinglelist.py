# Reverse a sublist within a list.
# Write a program which takes a singly linked list L and two integers
# s and f as arguments. Reverse the order of the nodes from the sth node
# to the fth node, inclusive. Numbering begins at 1. No allocation of
# additional nodes permitted.

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


# Book solution
def reverse_sublist(L, start, finish):
    # Make a dummy head to return dummy.next and a sublist head for the sublist
    # specify data as 0 and the next node as L (our node of interest linked list)
    dummy_head = sublist_head = ListNode(0, L)
    # from the head to the beginning of where we want to reverse
    # we will traverse it normally forwards
    for _ in range(1, start):
        sublist_head = sublist_head.next
    #this section we want to reverse
    sublist_iter = sublist_head.next
    # so for however many times it takes between the start to the finish
    # we start the reversing process
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next

# Write a function that reverses a singly linked list.
# Use no more than constant storage beyond that needed for the list itself.

# Still don't completely get it. Need to revisit.

def reverseList(L):
    #dummy_head = ListNode(0, L)
    prev = None
    current = L
    nex = L.next
    while (current is not None):
        current.next = prev
        prev = current
        current = nex
        if nex:
            nex = nex.next
    L = prev
    dummy_head = ListNode(0, L)
    return dummy_head.next

    #for _ in range(1):
    #    temp = L.next
    #    L.next = temp.next
    #    temp.next = list_head.next
    #    list_head.next = temp
    #return dummy_head.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
insert_after(a, b)
insert_after(b, c)
insert_after(c, d) 
insert_after(d, e) 
insert_after(e, f) 
printNode(reverseList(a))