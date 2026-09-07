# 💡 Logic
#
# We will use BFS (Breadth First Search) for this problem.
#
# BFS traverses the N-ary tree level by level.
#
# We use a queue to store the nodes that need to be processed.
#
# How it works:
#
# 1. If root is None, return an empty list.
# 2. Add the root node to the queue.
# 3. Find how many nodes are present in the current level.
# 4. Process exactly those nodes.
# 5. Add each node's value to the current level list.
# 6. Add all children of the current node to the queue.
# 7. Add the completed level to the result.
# 8. Repeat until the queue becomes empty.


# 🔄 Algorithm
#
# Queue = [root]
#
# while queue is not empty:
#
#     Find the number of nodes in the current level.
#
#     Create an empty list called level.
#
#     Process all nodes of the current level:
#         Remove one node from the queue.
#         Add node.val to level.
#         Add all children of the node to the queue.
#
#     Add level to result.
#
# Return result.


# 🧪 Dry Run
#
# Example:
#
#           1
#        /  |  \
#       3   2   4
#      / \
#     5   6
#
#
# Initially:
#
# Queue = [1]
# Result = []
#
#
# Level 1:
#
# Process node 1.
#
# Level = [1]
# Queue = [3, 2, 4]
#
# Result = [[1]]
#
#
# Level 2:
#
# Process nodes 3, 2, and 4.
#
# Level = [3, 2, 4]
#
# Node 3 has children 5 and 6.
#
# Queue = [5, 6]
#
# Result = [[1], [3, 2, 4]]
#
#
# Level 3:
#
# Process nodes 5 and 6.
#
# Level = [5, 6]
# Queue = []
#
# Result = [[1], [3, 2, 4], [5, 6]]
#
# The queue is now empty, so the traversal is complete.


# ⭐ Key Trick
#
# The most important trick is:
#
# level_size = len(queue)
#
# This tells us how many nodes belong to the current level.
#
# Then we process exactly that many nodes:
#
# for _ in range(level_size):
#
# This helps us keep every level in a separate list.


# ⏱️ Complexity
#
# Time Complexity: O(n)
#
# Every node is visited exactly once.
#
#
# Space Complexity: O(n)
#
# In the worst case, the queue can contain O(n) nodes.


# 🧑‍💻 Python Code

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        # If the tree is empty, return an empty list
        if root is None:
            return []

        # Create a queue for BFS traversal
        queue = deque([root])

        # Store the final answer
        result = []

        # Continue until the queue becomes empty
        while queue:

            # Get the number of nodes in the current level
            level_size = len(queue)

            # Store the values of the current level
            level = []

            # Process all nodes of the current level
            for _ in range(level_size):

                # Remove one node from the queue
                node = queue.popleft()

                # Add the node's value to the current level
                level.append(node.val)

                # Add all children of the current node to the queue
                for child in node.children:
                    queue.append(child)

            # Add the current level to the final result
            result.append(level)

        # Return the level order traversal
        return result


# ⭐ Most Important Line
#
# level_size = len(queue)
#
# It tells us how many nodes are present in the current level.
#
# For example:
#
# Queue = [3, 2, 4]
#
# level_size = 3
#
# So we process exactly 3 nodes.
#
# Their children are added to the queue,
# but they will be processed in the NEXT level.