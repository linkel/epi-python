# binary tree is either empty or a root node r together with a left tree and a right tree.
# subtrees are themselves binary trees. 

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# if l is the root of p's left subtree, we will say l is the left child of p,
# and p is the parent of l. 
# with the exception of the root, every node has a unique parent (??? is this true?)

# node object definition can include a parent field
# the search path is the unique sequence of nodes from the root to that node
# where each sequencec is a child of the previous node

# node is an ancestor if it lies on the search path. 
# d is the descendant of the node if the node is an ancestor of d.

# depth of a node n is the numbre of nodes on the search path from the root
# to n, not including n itself. height is the max depth of any node in the tree.
# level is all nodes at same depth.

# I have heard people say height and include that root node too. 

# A full binary tree is a tree where every node other than the leaves has 2 children.
# a perfect binary tree is a full tree where all leaves are at same depth
# and where every parent has two children. 

# a complete tree is a tree in which every level is completely filled and
# all nodes are as far left as possible. 

# The number of nonleaf nodes in a full binary tree is one less than the number of leaves.
# perfect binary tree of height h has 2^(h+1) - 1 nodes, of which
# 2^h are leaves. 
# Complete binary tree on n nodes has height floor of log(base 2)(n).
# In CS, base 2 is so ubiquitous that it seems like we assume log base 2 on these things...            

# Key computation on a binary tree is traversing all the nodes. 

# Inorder traversal:
# traverse the left
# traverse the root
# traverse the right

# Preorder traversal:
# traverse the root
# traverse the left
# traverse the right

# Postorder traversal:
# traverse the left
# traverse the right
# traverse the root

# Let T be a binary tree of n nodes with height h. Implemented recursively, these
# traversals are O(n) time and O(h) space. 

# Space complexity is dictated by the max depth of the function call stack.
# if each node has a parent field, the traversals can be done with O(1) additional
# space complexity. 

# implement three basic traversals:

def tree_traversal(root):
    if root:
        # pre order - root then left then right
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)
        # inorder - left then root then right
        print('Inorder: %d' % root.data)
        tree_traversal(root.right)
        # postorder - left then right then root
        print('Postorder: %d' % root.data)

leftBaby = BinaryTreeNode(10)
rightBaby = BinaryTreeNode(40)
myRoot = BinaryTreeNode(100,leftBaby,rightBaby)
tree_traversal(myRoot)

# time complexity is O(n) where n is # of nodes in tree
# call stack reaches max depth of h. So space is O(h).
# minimum value for h is log(n) for a complete binary tree,
# max is n for a skewed tree. 


# recursive algorithms tend to be well-suited for tree problems.
# remember to include space on the function call stack when doing
# space complexity analysis. 

# some tree problems have bf solutions using O(n) space, but
# there are subtler solutions that use existing tree nodes to use 
# O(1) space. 

# Consider left and right skewed trees when doing complexity analysis.
# note that O(h) where h is tree height translates into O(log n) for balanced trees
# and O(n) for skewed trees. 

# if each node has a parent field, use it to make your code simple and reduce
# time and space complexity.

# don't treat a node with a single child as a leaf!!! easy mistake. 



