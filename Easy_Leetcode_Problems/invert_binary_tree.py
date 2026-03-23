
# Approach:
# 1. If root is None, return None.
# 2. Swap the left and right child of current node.
# 3. Recursively invert the left subtree.
# 4. Recursively invert the right subtree.
# 5. Return the root.

# Logic:
# - Invert binary tree means mirror the tree.
# - For every node, left child becomes right child
#   and right child becomes left child.
# - We use recursion to apply this on every node.
# - Base case: if node is None, return None.
# - After swapping all nodes, return root.

# 7) Time and Space Complexity

# Time Complexity:
# O(n)
# Because we visit each node exactly once.

# Space Complexity:
# O(h)
# Due to recursion stack.
# h = height of the tree.


# 8) Interview / Viva Line (Short)

# Invert Binary Tree means making the tree a mirror image
# by swapping the left and right child of every node using recursion.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Swap left and right child
        root.left, root.right = root.right, root.left
        
        # Invert left subtree
        self.invertTree(root.left)
        
        # Invert right subtree
        self.invertTree(root.right)
        
        return root