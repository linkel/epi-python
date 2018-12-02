# A binary tree is symmetric if you can draw a line thru the root
# and the left is the mirror of the right. 
# structural symmetry vs symmetry, latter needs the values to be same too

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# symmetric test case
l3 = BinaryTreeNode(3)
l2 = BinaryTreeNode(2, None, l3)
l1 = BinaryTreeNode(6, None, l2)
r3 = BinaryTreeNode(3)
r2 = BinaryTreeNode(2, r3, None)
r1 = BinaryTreeNode(6, r2, None)

sym_root = BinaryTreeNode(314, l1, r1)

# asymmetric test case
al3 = BinaryTreeNode(3)
al2 = BinaryTreeNode(2, None, al3)
al1 = BinaryTreeNode(6, None, al2)
ar2 = BinaryTreeNode(2, None, None)
ar1 = BinaryTreeNode(6, ar2, None)
asym_root = BinaryTreeNode(314, al1, ar1)

empty_root = None
# test pair of subtrees for whether they are mirror images
# if they fail we return false and can stop checking

def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        return False
    return not tree or check_symmetric(tree.left, tree.right)

print(is_symmetric(sym_root))
print(is_symmetric(asym_root))
print(is_symmetric(empty_root))