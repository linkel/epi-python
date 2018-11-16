# queue is first in first out
# enqueue and dequeue are terms for add and remove
# a deque, pronounced like deck, is a doubly linked
# list where all insertions and deletions are from
# one of the two ends, so they're a bit like a deck of cards...(sort of)
# front insert is a push, back insert is an inject
# front delete is pop, back delete is eject

import collections 

class Queue:
    def __init__(self):
        self._data = collections.deque()
    
    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.popleft()

    def max(self):
        return max(self._data)

# O(1) to enqueue and dequeue
# O(n) to find max

# Queues are nice when order must be preserved.
