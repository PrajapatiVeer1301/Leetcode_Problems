# ---------- 💡 Logic ----------

# 1. Perform an inorder traversal.
#
# 2. First visit the left subtree.
#
# 3. Then visit the current/root node.
#
# 4. After visiting a node, decrease k.
#
# 5. If k == 0:
#       The current node is the kth smallest.
#
# 6. Then move to the right subtree.
#
# 7. Use a stack to perform iterative inorder traversal.


# ---------- 🔄 Algorithm ----------

# Step 1: Create an empty stack.
#
# Step 2: Set current = root.
#
# Step 3: While current is not None
#         OR stack is not empty:
#
#       a. Go to the leftmost node:
#
#          while current is not None:
#              stack.append(current)
#              current = current.left
#
#       b. Take the top node:
#
#          current = stack.pop()
#
#       c. Decrease k:
#
#          k -= 1
#
#       d. If k == 0:
#              return current.val
#
#       e. Move to the right subtree:
#
#          current = current.right


# ---------- 🧪 Dry Run ----------

# Input:
# root = [3,1,4,null,2]
# k = 1
#
# Tree:
#
#         3
#        / \
#       1   4
#        \
#         2
#
# --------------------------------
#
# stack = []
# current = 3
# k = 1
#
# --------------------------------
#
# Go left:
#
# Push 3:
# stack = [3]
#
# current = 1
#
# Push 1:
# stack = [3,1]
#
# current = None
#
# --------------------------------
#
# Pop:
#
# current = 1
# stack = [3]
#
# k = 1 - 1
#   = 0
#
# k == 0
#
# Therefore:
#
# return 1
#
# --------------------------------
#
# Final Answer:
#
# 1


# ---------- 🐍 Python Code ----------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        current = root

        while current is not None or stack:

            # Go to the leftmost node
            while current is not None:
                stack.append(current)
                current = current.left

            # Visit the node
            current = stack.pop()

            # Count the visited node
            k -= 1

            # If this is the kth node
            if k == 0:
                return current.val

            # Move to the right subtree
            current = current.right


# ---------- 🎯 Interview Explanation ----------

# I use the fact that inorder traversal of a BST
# gives values in sorted order.
#
# I perform inorder traversal iteratively using a stack.
#
# Every time I visit a node, I decrease k by 1.
#
# When k becomes 0, the current node is the kth
# smallest value, so I return its value.
#
# Time Complexity:
# O(H + k)
#
# H = height of the BST.
#
# Space Complexity:
# O(H)
#
# for the stack.


# ---------- ⭐ Key Trick ----------

# BST Inorder Traversal:
#
# Left → Root → Right
#
#        ↓
#
# Sorted Order
#
#        ↓
#
# kth visited node
#        ↓
#
# kth smallest value
#
#
# Remember:
#
# k = 1 → smallest value
#
# k = 2 → second smallest
#
# k = 3 → third smallest