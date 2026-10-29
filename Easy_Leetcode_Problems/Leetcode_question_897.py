
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:

        # ## LOGIC:
        # In-order traversal visits BST values in sorted order.
        # Create a new tree where every node has no left child.
        # Connect all nodes using their right pointers.

        # Store the nodes in sorted order.
        values = []

        # Perform in-order traversal.
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Create a dummy node to simplify building the tree.
        dummy = TreeNode(0)
        current = dummy

        # Create a right-only chain from sorted values.
        for value in values:
            current.right = TreeNode(value)
            current = current.right

        # Return the actual root, skipping the dummy node.
        return dummy.right


# ## EXAMPLE:
# Input: root = [5, 3, 6, 2, 4, None, 8, 1, None,
#                None, None, 7, 9]
#
# Output:
# [1, None, 2, None, 3, None, 4, None, 5,
#  None, 6, None, 7, None, 8, None, 9]

# ## DRY RUN:
# In-order traversal produces:
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Create the new tree:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
#
# Every left child is None.
# Every next node is connected using right.
#
# Final root = node with value 1

# ## ALGORITHM:
# 1. Perform in-order traversal of the BST.
# 2. Store node values in a list.
# 3. Create a dummy node.
# 4. Create a new node for every value.
# 5. Connect each new node using the right pointer.
# 6. Return dummy.right.

# ## INTERVIEW EXPLANATION:
# In-order traversal of a BST gives values in sorted order.
# I store these values and create a new tree using only
# right pointers. All left pointers remain None.
# Finally, I return the first actual node as the new root.

# ## KEY TRICK:
# In-order traversal = Left -> Root -> Right.
# Use dummy.right to return the new root.

# ## TIME COMPLEXITY:
# O(n), because every node is visited once.

# ## SPACE COMPLEXITY:
# O(n), for storing values and creating the new tree.
