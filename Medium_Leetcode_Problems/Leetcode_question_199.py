# Logic:
#
# 1. Use BFS (Level Order Traversal).
#
# 2. Process the binary tree level by level.
#
# 3. For every level, find the last node.
#
# 4. The last node of each level is
#    visible from the right side.
#
# 5. Add that node's value to result.
#
# Example:
#
#        1
#       / \
#      2   3
#       \   \
#        5   4
#
# Level 0 → [1]     → 1
# Level 1 → [2,3]   → 3
# Level 2 → [5,4]   → 4
#
# Answer = [1,3,4]

# Algorithm:
#
# 1. If root is None, return [].
#
# 2. Create a queue and add root.
#
# 3. While queue is not empty:
#
#       level_size = number of nodes
#                     in current level
#
# 4. Process all nodes of current level.
#
# 5. If current node is the last node
#    of the level:
#
#       Add node.val to result.
#
# 6. Add left and right children
#    to the queue.
#
# 7. Return result.

# Dry Run:
#
# Input:
# root = [1,2,3,null,5,null,4]
#
# Tree:
#
#        1
#       / \
#      2   3
#       \   \
#        5   4
#
# -------------------------
#
# Level 0:
#
# queue = [1]
# level_size = 1
#
# node = 1
# i = 0
#
# i == level_size - 1
# 0 == 0 → True
#
# result = [1]
#
# Add children 2 and 3
#
# queue = [2,3]
#
# -------------------------
#
# Level 1:
#
# queue = [2,3]
# level_size = 2
#
# node = 2
# i = 0
#
# 0 == 1 → False
#
# Add child 5
#
# node = 3
# i = 1
#
# 1 == 1 → True
#
# result = [1,3]
#
# Add child 4
#
# queue = [5,4]
#
# -------------------------
#
# Level 2:
#
# queue = [5,4]
# level_size = 2
#
# node = 5
# i = 0
#
# 0 == 1 → False
#
# node = 4
# i = 1
#
# 1 == 1 → True
#
# result = [1,3,4]
#
# -------------------------
#
# Final Answer:
#
# [1,3,4]

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result

# Interview Explanation:
#
# I used BFS or level-order traversal
# to process the tree level by level.
#
# For each level, I find the number
# of nodes present in that level.
#
# The last node processed in each level
# is the rightmost node, which is visible
# from the right side.
#
# Therefore, I add the last node's value
# of every level to the result.
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)


# ⭐ Important Line
if i == level_size - 1:
    result.append(node.val)