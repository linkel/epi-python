import collections
# test if binary tree is height balanced
# A binary tree is said to be height-balanced if the difference in height of 
# its left and right subtrees is at most one. 
# so a perfect and a complete binary tree are both height balanced. 
# Write a program that takes as input the root of a binary tree
# and checks whether the tree is height-balanced. 

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

leftBaby = BinaryTreeNode(10)
rightBaby = BinaryTreeNode(20)
root = BinaryTreeNode(0, leftBaby, rightBaby)

# brute force is to compute the height for tree at each node x recursively
# computer height for each node starting from leaves and go up
# check if difference in heights of left and right children is greater than 1
# uses O(n) storage and O(n) time. 

# we don't have to store the hts of all nodes at the same time.
# once we finish a subtree we just have to know if it's height balanced,
# then what its height is.

def is_bal(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )
    # first value of return indicates if balanced and if so
    # the second value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced