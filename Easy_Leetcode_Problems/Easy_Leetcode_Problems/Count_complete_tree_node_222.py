# Logic:
#
# 1. If the tree is empty,
#    return 0.
#
# 2. Calculate the height of
#    the leftmost path.
#
# 3. Calculate the height of
#    the rightmost path.
#
# 4. If both heights are equal,
#    the tree is a Perfect Binary Tree.
#
# 5. Use the formula:
#
#       Nodes = 2^height - 1
#
# 6. Otherwise, recursively count
#    the nodes in the left subtree
#    and right subtree.
#
# 7. Add 1 for the current root node.
#
# 8. Return the total number of nodes.

# Algorithm:
#
# 1. Check if the root is NULL.
#    If yes, return 0.
#
# 2. Find the left height of the tree.
#
# 3. Find the right height of the tree.
#
# 4. If left height == right height:
#       Return (2^height) - 1.
#
# 5. Otherwise:
#       Count nodes in the left subtree.
#       Count nodes in the right subtree.
#
# 6. Add 1 for the root node.
#
# 7. Return the total count.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        leftHeight = getLeftHeight(root)
        rightHeight = getRightHeight(root)

        # Perfect Binary Tree
        if leftHeight == rightHeight:
            return (2 ** leftHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
# Interview Explanation:
#
# 1. First, I calculate the leftmost
#    and rightmost heights of the tree.
#
# 2. If both heights are equal,
#    the tree is a Perfect Binary Tree.
#
# 3. I directly calculate the number
#    of nodes using the formula:
#
#       2^height - 1
#
# 4. Otherwise, I recursively count
#    the nodes in the left and right
#    subtrees and add 1 for the root.
#
# Time Complexity: O(log² n)
# Space Complexity: O(log n)