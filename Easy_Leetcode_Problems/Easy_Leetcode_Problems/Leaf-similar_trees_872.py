# Logic:
#
# 1. Traverse the first tree using DFS.
#
# 2. Store all leaf node values in a list.
#
# 3. Traverse the second tree using DFS.
#
# 4. Store all leaf node values in another list.
#
# 5. Compare both lists.
#
# 6. If both lists are equal,
#    return True.
#
# 7. Otherwise,
#    return False.

# Algorithm:
#
# 1. Create an empty list for Tree 1.
#
# 2. Create an empty list for Tree 2.
#
# 3. Perform DFS on Tree 1.
#
# 4. Whenever a leaf node is found,
#    add its value to the list.
#
# 5. Repeat the same for Tree 2.
#
# 6. Compare both leaf sequences.
#
# 7. Return True if equal,
#    otherwise False.

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeaves(root, leaves):

            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)

            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)

        leaves1 = []
        leaves2 = []

        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)

        return leaves1 == leaves2

# Interview Explanation:
#
# 1. I used DFS to traverse both trees.
#
# 2. Whenever I found a leaf node,
#    I stored its value in a list.
#
# 3. After traversing both trees,
#    I compared the two leaf sequences.
#
# 4. If they are equal,
#    I returned True.
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#
# where:
# n = nodes in first tree
# m = nodes in second tree