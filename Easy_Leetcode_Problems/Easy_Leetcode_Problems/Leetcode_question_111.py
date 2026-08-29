# 💡 Logic
#
# We use BFS (Breadth First Search) to find the minimum depth.
#
# BFS visits the binary tree level by level.
#
# The first leaf node we find will always be
# the nearest leaf node from the root.
#
# We store two things in the queue:
#
#     (node, depth)
#
# node  → current tree node
# depth → depth of that node
#
# If the current node has no left child
# and no right child, it is a leaf node.
#
# Therefore, we immediately return its depth.


# 🔄 Algorithm
#
# Step 1: If root is None:
#         return 0.
#
# Step 2: Create a queue.
#
#         queue = [(root, 1)]
#
# Step 3: While queue is not empty:
#
#         Remove the first node and its depth.
#
# Step 4: Check whether the current node is a leaf.
#
#         If:
#             node.left is None
#             AND
#             node.right is None
#
#         Then return depth.
#
# Step 5: If left child exists:
#
#         Add left child to the queue
#         with depth + 1.
#
# Step 6: If right child exists:
#
#         Add right child to the queue
#         with depth + 1.
#
# Step 7: Continue until the first leaf node is found.
#
# Step 8: Return the depth of the first leaf.


# 🧪 Dry Run
#
# Input:
#
# root = [3,9,20,null,null,15,7]
#
# Tree:
#
#         3
#        / \
#       9   20
#          /  \
#         15   7
#
# --------------------------------
#
# Initial:
#
# queue = [(3,1)]
#
# --------------------------------
#
# Level 1:
#
# Remove:
#
# node = 3
# depth = 1
#
# 3 is not a leaf because
# it has left and right children.
#
# Add its children:
#
# queue = [(9,2), (20,2)]
#
# --------------------------------
#
# Level 2:
#
# Remove:
#
# node = 9
# depth = 2
#
# 9 has:
#
# left = None
# right = None
#
# Therefore, 9 is a leaf.
#
# Return:
#
# depth = 2
#
# --------------------------------
#
# Final Answer:
#
# 2


# 🐍 Python Code
#
# from collections import deque
#
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#
#         # If tree is empty
#         if root is None:
#             return 0
#
#         # Queue stores:
#         # (node, depth)
#         queue = deque([(root, 1)])
#
#         while queue:
#
#             # Remove the first node
#             node, depth = queue.popleft()
#
#             # Check if current node is a leaf
#             if node.left is None and node.right is None:
#                 return depth
#
#             # Add left child if it exists
#             if node.left is not None:
#                 queue.append((node.left, depth + 1))
#
#             # Add right child if it exists
#             if node.right is not None:
#                 queue.append((node.right, depth + 1))
#
#         return 0


# 🎯 Interview Explanation
#
# I use BFS to find the minimum depth of the binary tree.
#
# BFS visits nodes level by level.
#
# Because of this, the first leaf node found by BFS
# will always be the nearest leaf from the root.
#
# I store each node together with its depth in a queue.
#
# When I find a node with no left and right children,
# it is a leaf node, so I immediately return its depth.
#
# Time Complexity: O(n)
#
# In the worst case, we may visit all nodes.
#
# Space Complexity: O(n)
#
# In the worst case, the queue can contain O(n) nodes.


# ⭐ Key Trick
#
# Binary Tree:
#
#         Root
#        /    \
#       ↓      ↓
#    Level 2  Level 2
#       ↓
#    Level 3
#
# BFS
#   ↓
# Visit level by level
#   ↓
# Find first leaf
#   ↓
# Return its depth
#   ↓
# Minimum Depth
#
#
# ⭐ Remember:
#
# Leaf Node =
# left == None AND right == None
#
# BFS → Minimum Depth