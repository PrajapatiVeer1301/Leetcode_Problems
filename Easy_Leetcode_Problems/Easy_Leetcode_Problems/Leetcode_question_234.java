// 💡 Logic
//
// We divide the linked list into two parts:
//
// 1. Use slow and fast pointers to find the middle node.
//
// 2. Reverse the second half of the linked list.
//
// 3. Compare the first half with the reversed second half.
//
// 4. If any value is different:
//       return false;
//
// 5. If all values are the same:
//       return true;
//
//
// --------------------------------
//
// Example:
//
// 1 → 2 → 2 → 1
//
// First half:
// 1 → 2
//
// Second half:
// 2 → 1
//
// Reverse second half:
// 1 → 2
//
// Compare:
//
// 1 == 1 ✅
// 2 == 2 ✅
//
// Answer = true


// 🔄 Algorithm
//
// Step 1: Initialize two pointers:
//
//         slow = head
//         fast = head
//
// Step 2: Find the middle of the linked list.
//
//         slow moves one step.
//         fast moves two steps.
//
//         while (fast != null && fast.next != null) {
//             slow = slow.next;
//             fast = fast.next.next;
//         }
//
// Step 3: After the loop,
//         slow points to the beginning of the
//         second half.
//
// Step 4: Reverse the second half.
//
//         previous = null;
//
//         while (slow != null) {
//             nextNode = slow.next;
//             slow.next = previous;
//             previous = slow;
//             slow = nextNode;
//         }
//
// Step 5: After reversing:
//
//         previous = head of reversed second half.
//
// Step 6: Set two pointers:
//
//         left = head;
//         right = previous;
//
// Step 7: Compare both halves.
//
//         while (right != null) {
//
//             if (left.val != right.val) {
//                 return false;
//             }
//
//             left = left.next;
//             right = right.next;
//         }
//
// Step 8: If all values match:
//
//         return true;


// 🧪 Dry Run
//
// Input:
//
// head = [1,2,2,1]
//
// Linked List:
//
// 1 → 2 → 2 → 1 → null
//
// --------------------------------
//
// Step 1: Find middle
//
// slow = 1
// fast = 1
//
// Move:
//
// slow = 2
// fast = 2
//
// Move:
//
// slow = 2
// fast = null
//
// Therefore:
//
// slow points to the second half:
//
// 2 → 1
//
// --------------------------------
//
// Step 2: Reverse second half
//
// Before:
//
// 2 → 1 → null
//
// After:
//
// 1 → 2 → null
//
// previous = 1
//
// --------------------------------
//
// Step 3: Compare both halves
//
// left = 1
// right = 1
//
// 1 == 1 ✅
//
// Move:
//
// left = 2
// right = 2
//
// 2 == 2 ✅
//
// Move:
//
// right = null
//
// --------------------------------
//
// All values matched.
//
// Final Answer:
//
// true


// ☕ Java Code
//
// Definition for singly-linked list.
//
// class ListNode {
//     int val;
//     ListNode next;
//
//     ListNode() {}
//
//     ListNode(int val) {
//         this.val = val;
//     }
//
//     ListNode(int val, ListNode next) {
//         this.val = val;
//         this.next = next;
//     }
// }

class Solution {
    public boolean isPalindrome(ListNode head) {

        // Step 1: Find the middle of the linked list
        ListNode slow = head;
        ListNode fast = head;

        // slow moves one step
        // fast moves two steps
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse the second half
        ListNode previous = null;

        while (slow != null) {

            // Store the next node
            ListNode nextNode = slow.next;

            // Reverse the pointer
            slow.next = previous;

            // Move previous forward
            previous = slow;

            // Move slow forward
            slow = nextNode;
        }

        // previous is now the head of
        // the reversed second half

        // Step 3: Compare both halves
        ListNode left = head;
        ListNode right = previous;

        while (right != null) {

            // If values are different,
            // it is not a palindrome
            if (left.val != right.val) {
                return false;
            }

            // Move both pointers
            left = left.next;
            right = right.next;
        }

        // All values are the same
        return true;
    }
}


// 🎯 Interview Explanation
//
// I use the two-pointer technique to find the middle
// of the linked list.
//
// The slow pointer moves one step at a time,
// while the fast pointer moves two steps at a time.
//
// When fast reaches the end, slow is at the middle.
//
// Then I reverse the second half of the linked list.
//
// After reversing, I compare the first half with
// the reversed second half.
//
// If any two corresponding values are different,
// I return false.
//
// If all values match, I return true.
//
// This solution does not use an extra array or stack.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)


// ⭐ Key Trick
//
// slow → finds the middle
// fast → moves twice as fast
//
// --------------------------------
//
// Then:
//
// Reverse second half
//        ↓
// Compare both halves
//
// --------------------------------
//
// Example:
//
// 1 → 2 → 2 → 1
//
// First half:
// 1 → 2
//
// Second half:
// 2 → 1
//
// Reversed second half:
// 1 → 2
//
// Compare:
//
// 1 == 1 ✅
// 2 == 2 ✅
//
// Answer = true
//
// --------------------------------
//
// ⭐ Remember:
//
// slow = slow.next;
// fast = fast.next.next;
//
// These two pointers help us find the middle
// of the linked list.
//
// To reverse:
//
// nextNode = slow.next;
// slow.next = previous;
// previous = slow;
// slow = nextNode;
//
// Finally:
//
// Compare:
//
// left.val == right.val
//
// If different → false
// If all same → true
//
// --------------------------------
//
// Complexity:
//
// Time  → O(n)
// Space → O(1)