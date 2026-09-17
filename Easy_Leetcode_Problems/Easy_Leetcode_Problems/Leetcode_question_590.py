# 💡 Iterative Logic
#
# The question specifically asks:
# The recursive solution is trivial, can you solve it iteratively?
#
# So, we will use a Stack.
#
# Normally, Preorder Traversal is:
#
# Parent → Children
#
# But we need Postorder Traversal:
#
# Children → Parent
#
#
# ⭐ Key Trick
#
# First, we process the node and add its value to the result.
# Then, we push all of its children into the stack.
#
# This gives us Reverse Postorder:
#
# 1 → 4 → 2 → 3 → 6 → 5
#
# Then, we reverse the result:
#
# 5 → 6 → 3 → 2 → 4 → 1
#
# This is the required Postorder Traversal. ✅
#
#
# 🔄 Algorithm
#
# 1. If root == None, return [].
#
# 2. Push root into the stack.
#
# 3. While the stack is not empty:
#    - Remove the top node from the stack.
#    - Add its value to the result.
#    - Push all its children into the stack.
#
# 4. Reverse the result using result.reverse().
#
# 5. Return the result.
#
#
# 🧑‍💻 Python Code
#
# class Solution:
#
#     def postorder(self, root: 'Node') -> List[int]:
#
#         # If tree is empty, return an empty list
#         if root is None:
#             return []
#
#         # Stack is used for iterative traversal
#         stack = [root]
#
#         # Store the traversal result
#         result = []
#
#         # Process nodes until the stack becomes empty
#         while stack:
#
#             # Remove the top node from the stack
#             node = stack.pop()
#
#             # Add the node value to the result
#             result.append(node.val)
#
#             # Add all children to the stack
#             for child in node.children:
#                 stack.append(child)
#
#         # Reverse the result to get Postorder Traversal
#         result.reverse()
#
#         return result
#
#
# 🧪 Dry Run
#
# For:
#
#         1
#       / | \
#      3  2  4
#     / \
#    5   6
#
#
# Initially:
#
# stack = [1]
# result = []
#
#
# Process 1:
#
# stack = [3, 2, 4]
# result = [1]
#
#
# Process 4:
#
# result = [1, 4]
#
#
# Process 2:
#
# result = [1, 4, 2]
#
#
# Process 3:
#
# stack = [5, 6]
# result = [1, 4, 2, 3]
#
#
# Process 6:
#
# result = [1, 4, 2, 3, 6]
#
#
# Process 5:
#
# result = [1, 4, 2, 3, 6, 5]
#
#
# Now reverse the result:
#
# [5, 6, 3, 2, 4, 1]
#
#
# ✅ Final Answer
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)
#
# Where n = total number of nodes in the tree.
#
#
# 🎯 Interview Explanation
#
# "I use a stack to perform a modified preorder traversal.
# I store the nodes in Parent → Children order and then
# reverse the result to obtain Children → Parent,
# which is Postorder Traversal."