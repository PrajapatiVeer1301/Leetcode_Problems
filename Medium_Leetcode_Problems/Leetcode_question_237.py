# Logic:
#
# We cannot access the previous node.
#
# So, we copy the value of the next node
# into the current node.
#
# Then we skip the next node.
#
# Example:
#
# Before:
#
# 4 → 5 → 1 → 9
#     ↑
#    node
#
# Step 1:
# Copy next node's value:
#
# 4 → 1 → 1 → 9
#
# Step 2:
# Skip the next node:
#
# 4 → 1 → 9
#
# Main idea:
#
# node.val = node.next.val
# node.next = node.next.next

# Algorithm:
#
# 1. Copy the value of node.next
#    into node.
#
# 2. Change node.next to node.next.next.
#
# 3. The next node is skipped.
#
# 4. The given node now contains the
#    next node's value.
#
# 5. No return value is required.



# Input:
#
# head = [4,5,1,9]
# node = 5
#
# Linked List:
#
# 4 → 5 → 1 → 9
#     ↑
#    node
#
# -------------------------
#
# Step 1:
#
# node.val = node.next.val
#
# node.next.val = 1
#
# So:
#
# 4 → 1 → 1 → 9
#
# -------------------------
#
# Step 2:
#
# node.next = node.next.next
#
# The first 1 is skipped.
#
# Final:
#
# 4 → 1 → 9
#
# -------------------------
#
# Output:
#
# [4,1,9]

class Solution:
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next


# Interview Explanation:
#
# Since the head and previous node are not given,
# I cannot directly remove the given node.
#
# The given node is guaranteed not to be the
# last node, so I use its next node.
#
# First, I copy the next node's value into
# the current node.
#
# Then, I make the current node point to
# the node after the next node.
#
# This effectively removes the next node
# and makes the given node represent it.
#
# Time Complexity: O(1)
#
# Space Complexity: O(1)


