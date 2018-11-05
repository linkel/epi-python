# Design a stack that includes a max operation in addition to push and pop.
# The max method should return the maximum value stored in the stack.

# Simplest way to implement a max op is to iterate through the array for
# an array-based stack. Time complexity would be O(n) and the space would be
# O(1) where n is the # of elements in the stack.

# Time complexity could be reduced to O(log n) using auxiliary data structures,
# like a heap or a binary search tree or a hash table. Space will increase to
# O(n) and get complicated code.

# What if we use just one variable, M, to record the element that's the max
# in the stack? Updating M on pushes is easy, M = max(M, e). 
# But updating M on pop is harder. If M gets popped we don't know what the
# next biggest is. 

# Let's cache the max stored at or below each entry in the stack. 
# 

import collections
class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(
                x, self.max())))
        
newStack = Stack()
newStack.push(1)
newStack.push(3)
newStack.push(9)
print(newStack.max())
print(newStack.pop())
print(newStack.max())


# Can improve on the best-case space needed since if an element e
# being pushed is smaller than the max element already in the stack, then
# e can never be the maximum, so we do not need to record it.
# Can't store the sequence of max values in a separate stack because
# of duplicates. So we can record the number of occurences of each max value.

class StackCount:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count
    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element
    
    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x,1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x,1))

    