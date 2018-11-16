# Given a binary tree, return an array consisting of keys at the same level.
# Keys should appear in the order of the nodes' depths. 

# Pair of queues...

# Brute force method can write nodes into array while calculating depth.
# Preorder traversal will ensure that nodes at the same depth are sorted
# from left to right. Then can sort the array using node depth as sort key. 
# Time complexity would be O(n log n) and space O(n) for node depth storage.

# But since nodes are already somewhat ordered, we could reduce time comp.

# What if we used a queue of nodes to store nodes at depth i and aq ueue at depth i + 1?

def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child 
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child 
        ]
    return result


# Write a program which takes as input a binary tree and returns the keys in top down,
# alternating left to right and right to left order, starting from left to right.

