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

# Had to look up info to write this.

def reverseList(L):
    #dummy_head = ListNode(0, L)
    prev = None
    current = L
    nex = L.next
    # as long as there is a node at the pointer current, keep going
    while (current is not None):
        current.next = prev
        prev = current
        current = nex
        # if nex exists then go to the next (otherwise nonetype has no next)
        if nex:
            nex = nex.next
    # set the new head of the linked list
    L = prev
    # dummy head at the end so that it points to the new start of the list
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
g = ListNode(7)
insert_after(a, b)
insert_after(b, c)
insert_after(c, d) 
insert_after(d, e) 
insert_after(e, f) 
insert_after(f,g)
#printNode(reverseList(a))

# Write a program which takes as input a singly linked list L
# and a nonnegative integer k and reverses the list k nodes at a time
# if the nodes in the list is not a multiple of k
# leave the last n mod k nodes unchanged. Do not change any data.

# attempt: unfortunately it is nonfunctional and also does not swap by k nodes,
# the way the problem is worded. It tries to swap
# but will end up changing 2 in overlap
def reversemod(L, k):
    '''L: singly linked list
    k: nonnegative integer'''
    checker = current = L
    prev = None
    nex = L.next
    itsOver = False
    while current is not None:
        incrementToForward = 0
        for _ in range(k-1):
            if checker is not None:
                checker = checker.next
                incrementToForward += 1
            else:
                itsOver = True
        if itsOver == False:
            for _ in range(incrementToForward):
                current.next = checker.next # need to check for the next that it exists tho
                prev = current
                current = nex
                if nex:
                    nex = nex.next
        elif itsOver == True:
            break
    L = prev
    dummy_head = ListNode(0, L)
    return dummy_head.next

printNode(a)
printNode(reversemod(a, 2))

# solution found with help from internet
# still need to go over this, I don't understand how the
# reversing occurs at the cur.next, cur, pre = pre, cur.next, cur part.
    
def reverseGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1 # r will keep going til count becomes k
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next