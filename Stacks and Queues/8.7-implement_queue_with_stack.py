# I remember seeing this problem before. 
# The conceit is that a queue is FIFO and a stack is LIFO (last in, first out). 
# You can't use a single stack to accomplish this (well, maybe someone out there has done some 
# very extravagant thing to technically use a stingle stack), but you can do this
# with two stacks! 

# One stack is going to be for items coming in and no pops have happened.
# When a pop is requested, we take everything out of the stack and put it all into the other stack, and pop an item off the 2nd stack.
# Now everything in the 2nd stack is in order "correctly" for a queue so we can keep popping off of it til it is empty
# at which point we can grab stuff off the top again. 

# The book's solution notes the less efficient method first, which is to do the 
# queuing and popping more times to keep stuff in the first stack.

class Queue:
    def __init__(self):
        self.enter = []
        self.exit = []
    def enqueue(self, x):
        self.enter.append(x)
    def dequeue(self):
        if not self.exit:
            while self.enter:
                self.exit.append(self.enter.pop())
        # after we've moved everything over and it's still empty we're actually out
        if not self.exit:
            print("Yo we're out of items")
            return
        return self.exit.pop()


