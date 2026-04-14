
# Logic:
# Use two pointers: slow and fast
# slow moves 1 step at a time
# fast moves 2 steps at a time
# If there is a cycle, fast will eventually meet slow
# If there is no cycle, fast will reach None
# If slow == fast, return True
# If loop ends, return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Approach:
        # Use Floyd's Cycle Detection Algorithm (Tortoise and Hare)
        # Take two pointers: slow and fast
        # slow moves one node at a time
        # fast moves two nodes at a time
        
        # Logic:
        # If linked list has a cycle, slow and fast will meet
        # If linked list has no cycle, fast or fast.next becomes None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(1)
