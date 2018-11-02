# Without knowing the length of a linked list it isn't trival to
# delete the kth last element in a singly linked list.
# Given a singly linked list and an integer k, write a program to remove
# the kth last element from the list. 

# Not allowed to use more than a few words of storage. Cannot assume 
# it is possible to record the length of the list. 

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

f = ListNode(6)
e = ListNode(5,f)
d = ListNode(4,e)
c = ListNode(3, d) 
b = ListNode(2, c)
a = ListNode(1, b)

def print_nodes(node):
    temp = node
    print(temp.data)
    while temp.next:
        temp = temp.next
        print(temp.data)

print_nodes(a)

def remove_kth(node, k):
    iter1 = node
    iterend = node
    for _ in range(k):
        # TODO: error case for if the linked list isn't as long as k
        iterend = iterend.next
        # iterend travels a bit in first
    while iterend != None:
        iter1 = iter1.next
        iterend = iterend.next
    if iterend == None:
        iter1.data = iter1.next.data
        iter1.next = iter1.next.next
    
#remove_kth(a, 1)
#print_nodes(a)

# whoops this above one I wrote only works if k isn't 1! it uses the O(1)
# deletion method. I need to write one where k being 1 is okay. 

# this next one should be able to delete for all k > 0

def remove_kth_safe(node, k):
    iter1 = iterend = node
    for _ in range(k):
        iterend = iterend.next
    while iterend.next != None:
        iter1 = iter1.next
        iterend = iterend.next
    # when iterend.next is equal to None then iter1 is at k+1
    if iterend.next == None:
        iter1.next = iter1.next.next

remove_kth_safe(a, 3)
print_nodes(a)

# It works! nice! 

# Brute force approach is to compute the length with one pass and then
# use it to detremine which node to delete in second pass.

# Book solution below:
# Assumes L has at least k nodes

def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the k + 1 th last node, deletes successor
    second.next = second.next.next
    return dummy_head.next

# book solution uses a dummy head and returns it 

# time complexity is O(n) where ni s length of list.
# space is O(1)

#remove_kth_last(a, 3)
#print_nodes(a)