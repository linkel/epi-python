# Consider two singly linked lists in which each node holds a number.
# Assume the lists are sorted, so that numbers appear ascending order within
# each list. The merge of the two lists is a list consiting of the nodes of 
# the two lists in which numbers appear in ascending order.

# for example, L1 has 2 -> 5 -> 7 -> null
# and L2 has 3 -> 11 -> null
# then the merge is 2 -> 3 -> -> 5 -> 7 -> 11 -> null

# Write a program that takes two lists, assumed to be sorted, and
# returns their merge.

# Naive approach is to append the lists together then sort.
# But then the time complexity becomes O((n+m)log(n+m))
# So a better way is to traverse the two lists and choose the 
# smaller of the keys to continue traversing from.


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

def mergeTwo(L1, L2):
    # dummy head as placeholder for the result
    dummyHead = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    tail.next = L1 or L2
    return dummyHead.next

#x = ListNode(1)
#x1 = ListNode(4)
#y = ListNode(3)

#insert_after(x, x1)
#printNode(x)
#z = mergeTwo(x, y)
#printNode(x)

# the or in the assignment above is to select a nonempty object
# so if L1 is None then it would go to L2

# Solve the same problem when the lists are doubly linked. 

class DoublyListNode:
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def insert_after_Doubly(node, new_node):
    new_node.next = node.next
    new_node.prev = node
    node.next = new_node
    # no change to node.prev

def delete_after_Doubly(node):
    # does this make sense?
    # if the node after the next one exists,
    # then make its prev the current one, not the next since we're deleting that
    if node.next.next != None:
        node.next.next.prev = node
    node.next = node.next.next
    
def printNode_Doubly(node):
    temp = node
    print(temp.data)
    while temp.next:
        temp = temp.next
        print(temp.data)

a = DoublyListNode(1)
b = DoublyListNode(3)
c = DoublyListNode(5)
d = DoublyListNode(7)

insert_after_Doubly(a,b)
insert_after_Doubly(b,c)
insert_after_Doubly(c,d)


#printNode_Doubly(a)
#delete_after_Doubly(b)
#printNode_Doubly(a)

# The below is not completely working. Can't seem to write the correct
# previous node in. I will revisit it later.

def mergeDoubly(L1, L2):
    dummyHead = tail = DoublyListNode()
    #temp = DoublyListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            tail.next.prev = tail
            #L1.next.prev = L1
            L1 = L1.next
        else:
            tail.next = L2
            tail.next.prev = tail
            #L2.next.prev = L2
            L2 = L2.next
        #tail.next.prev = tail
        tail = tail.next
    tail.next = L1 or L2
    return dummyHead.next

e = DoublyListNode(2)
f = DoublyListNode(4)
g = DoublyListNode(6)
h = DoublyListNode(8)

insert_after_Doubly(e,f)
insert_after_Doubly(f,g)
insert_after_Doubly(g,h)

#printNode_Doubly(e)
superNode = mergeDoubly(a, e)
#printNode_Doubly(superNode)


printNode_Doubly(h.prev)



#i = DoublyListNode(2)
#j = DoublyListNode(4)
#k = DoublyListNode(6)
#l = DoublyListNode(8)

#insert_after_Doubly(i,j)
#insert_after_Doubly(j,k)
#insert_after_Doubly(k,l)

#printNode_Doubly(l.prev)