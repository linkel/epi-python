# Remove duplicates from a sorted list of integers in a singly linked list. 
# linked list remains sorted after.
# ex: 2 2 3 5 7 11 11 to 2 3 5 7 11

# Looking at it from a brute force perspective, you could create a new list,
# and use a hashtable/dictionary to see if a value has already been added to the new list.
# this would use up space for the dictionary in proportion to the sized
# of the linked list, and make a new linked list with size O(n).

# If we chose to search in the new linked list for values that repeated and remove those,
# it saves on memory (since we can discard the hash table) but it uses up O(n^2) for the lookups
# since we'd traverse the original list and traverse the new one as well each time.

# Since this list is sorted, we can actually just remove successive nodes with
# the same value as the current node.

def remove_dupes(L):
    it = L # we keep the reference to the original so we can return it later
    while it: # this while will break if it becomes None
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data: #short circuit eval
            next_distinct = next_distinct.next # this is how we "delete", by skipping the next node
        it.next = next_distinct
        it = next_distinct
    return L
