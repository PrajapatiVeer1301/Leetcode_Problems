
## Explanation in Short (for interview / viva)

# 1. Create a dummy node before the head
# 2. Use current pointer to traverse
# 3. If current.next.val == val, skip that node
# 4. Else move current forward
# 5. Return dummy.next as new head

# Approach:

# We use a dummy node before the head to handle deletion easily,
# especially when the head node itself needs to be removed.
#
# Traverse the linked list using a pointer 'current'.
# If current.next.val == val, remove that node by skipping it:
# current.next = current.next.next
# Otherwise, move current forward.
#
# Finally, return dummy.next as the new head.

# Logic:

# 1. Create a dummy node before the head node.
#    This helps handle cases where the head itself needs to be deleted.
#
# 2. Point dummy.next to the original head.
#
# 3. Use a pointer 'current' starting from dummy.
#
# 4. Traverse the linked list while current.next exists.
#
# 5. If current.next.val == val:
#       Remove that node by linking current.next to current.next.next
#       (skip the node having the target value)
#
# 6. Else:
#       Move current to the next node
#
# 7. After traversal, return dummy.next
#    because dummy.next will be the new head of the updated list.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
    
    