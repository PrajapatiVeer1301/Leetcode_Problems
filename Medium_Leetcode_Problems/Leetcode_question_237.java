// Logic:
//
// We are not given the head or the previous node.
//
// So, we cannot directly delete the given node.
//
// The given node is guaranteed not to be the last node.
//
// Therefore:
//
// 1. Copy the value of the next node
//    into the current node.
//
// 2. Skip the next node.
//
// Example:
//
// Before:
//
// 4 → 5 → 1 → 9
//     ↑
//    node
//
// Step 1:
//
// 4 → 1 → 1 → 9
//
// Step 2:
//
// 4 → 1 → 9
//
// Main idea:
//
// node.val = node.next.val;
// node.next = node.next.next;


// Algorithm:
//
// 1. Set current node's value equal to
//    the next node's value.
//
// 2. Set current node's next pointer to
//    next node's next pointer.
//
// 3. The next node is skipped.
//
// 4. No value needs to be returned.


// Input:
//
// 4 → 5 → 1 → 9
//     ↑
//    node
//
// -------------------------
//
// Step 1:
//
// node.val = node.next.val;
//
// node.val = 1;
//
// List:
//
// 4 → 1 → 1 → 9
//
// -------------------------
//
// Step 2:
//
// node.next = node.next.next;
//
// List:
//
// 4 → 1 → 9
//
// -------------------------
//
// Final Output:
//
// [4,1,9]


class Solution {

    public void deleteNode(ListNode node) {

        node.val = node.next.val;
        node.next = node.next.next;
    }
}

// Interview Explanation:
//
// Since the previous node and head are not given,
// I cannot directly remove the given node.
//
// The given node is guaranteed not to be the tail,
// so I use its next node.
//
// First, I copy the next node's value into
// the current node.
//
// Then I skip the next node by changing
// the next pointer.
//
// This effectively deletes the given node.
//
// Time Complexity: O(1)
//
// Space Complexity: O(1)


