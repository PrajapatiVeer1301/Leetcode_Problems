# Logic:
#
# 1. If the tree is empty,
#    return 0.
#
# 2. Visit every child of the current node.
#
# 3. Find the maximum depth among all children.
#
# 4. Add 1 for the current node.
#
# 5. Return the maximum depth.

# Algorithm:
#
# 1. Check if root is None.
#    If yes, return 0.
#
# 2. Initialize max_depth = 0.
#
# 3. Traverse all children.
#
# 4. Recursively calculate
#    each child's depth.
#
# 5. Store the maximum depth.
#
# 6. Return max_depth + 1.


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root is None:
            return 0

        max_depth = 0

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))

        return max_depth + 1
    
# Interview Explanation:
#
# 1. I used Depth First Search (DFS) with recursion.
#
# 2. If the current node is None,
#    I return 0.
#
# 3. Otherwise, I recursively calculate
#    the depth of each child.
#
# 4. I keep track of the maximum depth
#    among all children.
#
# 5. Finally, I add 1 for the current node
#    and return the result.
#
# Time Complexity: O(n)
# Space Complexity: O(h)
#
# where:
# n = number of nodes
# h = height of the tree