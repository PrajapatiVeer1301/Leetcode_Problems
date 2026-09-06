# 💡 Logic
#
# We need to find the leftmost value in the last row of a binary tree.
#
# We will use BFS (Breadth-First Search).
#
# BFS visits the tree level by level.
#
# Example:
#
#         1              ← Level 1
#        / \
#       2   3            ← Level 2
#      /     \
#     4       5          ← Level 3
#
# For every level, the first node is the leftmost node of that level.
#
# If we keep updating the answer with the first node of every level,
# the last updated value will be the leftmost value of the last level.


# 🔄 Algorithm
#
# 1. Put the root node into a queue.
#
# 2. Set answer = root.val.
#
# 3. While the queue is not empty:
#
#    - Find the number of nodes in the current level using len(queue).
#
#    - Process all nodes of the current level.
#
#    - If i == 0, this is the first node of the current level,
#      so store its value in answer.
#
#    - Add the left child to the queue if it exists.
#
#    - Add the right child to the queue if it exists.
#
# 4. After all levels are processed, return answer.
#
# 5. Since the last level is processed last,
#    answer will contain the leftmost value of the last row.


# 🧪 Dry Run
#
# Example:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
#
# Level 1:
#
# Queue = [1]
#
# First node = 1
# answer = 1
#
# Add children of 1:
#
# Queue = [2, 3]
#
#
# --------------------------------
#
# Level 2:
#
# Queue = [2, 3]
#
# First node = 2
# answer = 2
#
# Add children:
#
# Queue = [4, 5, 6]
#
#
# --------------------------------
#
# Level 3:
#
# Queue = [4, 5, 6]
#
# First node = 4
# answer = 4
#
# Add children:
#
# Queue = [7]
#
#
# --------------------------------
#
# Level 4:
#
# Queue = [7]
#
# First node = 7
# answer = 7
#
# Queue becomes empty.
#
# Traversal is complete.
#
# Final Answer = 7


# 🎯 Interview Explanation
#
# "I will use BFS because BFS processes the binary tree level by level.
#
# For every level, I identify the first node as the leftmost node.
#
# I update the answer whenever I process the first node of a level.
#
# Since BFS processes levels from top to bottom, the last value stored
# in answer will be the leftmost value of the last level.
#
# Finally, I return that value."


# ⭐ Key Trick
#
# The key trick is:
#
# BFS + first node of every level
#
# The condition:
#
# if i == 0:
#     answer = node.val
#
# means that we are taking the first node of each level.
#
# The first node of the final level is exactly the bottom-left value.


# ⏱️ Complexity
#
# Time Complexity:
# O(n)
#
# Every node is visited exactly once.
#
#
# Space Complexity:
# O(n)
#
# The queue can contain up to O(n) nodes in the worst case.


# 🧑‍💻 Python Code

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # Create a queue and add the root
        queue = deque([root])

        # Initially, the answer is the root value
        answer = root.val

        # Process the tree level by level
        while queue:

            # Get the number of nodes in the current level
            level_size = len(queue)

            # Process every node in the current level
            for i in range(level_size):

                # Remove the first node from the queue
                node = queue.popleft()

                # If this is the first node of the level,
                # it is the leftmost node of that level
                if i == 0:
                    answer = node.val

                # Add the left child if it exists
                if node.left:
                    queue.append(node.left)

                # Add the right child if it exists
                if node.right:
                    queue.append(node.right)

        # Return the leftmost value of the last level
        return answer