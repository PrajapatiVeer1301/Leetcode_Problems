
# ------------------------------------------------------------
#  Merge Two Binary Trees  (LeetCode 617)
# ------------------------------------------------------------

# Algorithm:
#
# 1. If root1 is None, return root2.
#
# 2. If root2 is None, return root1.
#
# 3. Add the value of root2 to root1.
#
# 4. Recursively merge the left children of both trees.
#
# 5. Recursively merge the right children of both trees.
#
# 6. Return the merged tree (root1).

# Logic:
#
# 1. Check if root1 is None.
#    - If yes, return root2 because there is nothing to merge.
#
# 2. Check if root2 is None.
#    - If yes, return root1 because there is nothing to merge.
#
# 3. If both nodes exist:
#    - Add root2's value to root1's value.
#
# 4. Recursively merge the left child of both trees.
#
# 5. Recursively merge the right child of both trees.
#
# 6. Return the merged tree (root1).
#
# Time Complexity: O(n)
# Space Complexity: O(h)
# where n = total number of nodes and h = height of the tree.

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
    

# Interview Explanation (1 Minute)
# 1. Start merging from the root nodes of both trees.
# 2. If one node is None, return the other node.
# 3. If both nodes exist, add their values.
# 4. Recursively merge the left children.
# 5. Recursively merge the right children.
# 6. Return the merged tree.

