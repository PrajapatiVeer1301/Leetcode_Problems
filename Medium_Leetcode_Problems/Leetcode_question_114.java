// 💡 Logic
//
// We will flatten the binary tree in-place.
//
// The final structure should follow preorder traversal:
//
// Preorder = Root → Left → Right
//
// Every node will have:
//
//     left = null
//
// and the right pointer will point to the next node.
//
// For every current node:
//
// 1. If current.left is null:
//       Move to current.right.
//
// 2. If current.left exists:
//
//       a. Find the rightmost node of the left subtree.
//
//       b. Connect the original right subtree
//          to this rightmost node.
//
//       c. Move the left subtree to current.right.
//
//       d. Set current.left = null.
//
//       e. Move to current.right.
//
// This keeps all nodes in preorder order.
//
//
// 🔄 Algorithm
//
// Step 1: Set:
//
//         current = root
//
// Step 2: While current is not null:
//
// Step 3: If current.left is null:
//
//         Move current to current.right.
//
//         current = current.right
//
// Step 4: Otherwise:
//
//         Store the left subtree:
//
//         leftSubtree = current.left
//
// Step 5: Find the rightmost node
//         of the left subtree:
//
//         predecessor = leftSubtree
//
//         while predecessor.right is not null:
//             predecessor = predecessor.right
//
// Step 6: Connect the original right subtree:
//
//         predecessor.right = current.right
//
// Step 7: Move the left subtree to the right:
//
//         current.right = current.left
//
// Step 8: Remove the left pointer:
//
//         current.left = null
//
// Step 9: Move to the next node:
//
//         current = current.right
//
// Step 10: Continue until current becomes null.
//
//
// 🧪 Dry Run
//
// Input:
//
//         1
//        / \
//       2   5
//      / \   \
//     3   4   6
//
// --------------------------------
//
// current = 1
//
// 1 has a left subtree:
//
//         2
//        / \
//       3   4
//
// Find the rightmost node of left subtree:
//
// predecessor = 4
//
// Original right subtree:
//
// 5 → 6
//
// Connect:
//
// 4.right = 5
//
// Move left subtree to right:
//
// 1.right = 2
//
// Remove left:
//
// 1.left = null
//
// Structure becomes:
//
// 1 → 2
//     / \
//    3   4 → 5 → 6
//
// --------------------------------
//
// current = 2
//
// 2 has a left subtree:
//
//     2
//    /
//   3
//
// Rightmost node:
//
// predecessor = 3
//
// Original right subtree:
//
// 4 → 5 → 6
//
// Connect:
//
// 3.right = 4
//
// Move left subtree to right:
//
// 2.right = 3
//
// Remove left:
//
// 2.left = null
//
// Now:
//
// 1 → 2 → 3 → 4 → 5 → 6
//
// --------------------------------
//
// Continue moving current to the right.
//
// All remaining nodes have no left child.
//
// --------------------------------
//
// Final:
//
// 1 → 2 → 3 → 4 → 5 → 6
//
// left pointer of every node = null
//
//
// ☕ Java Code
//
// Definition for a binary tree node.
// class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//
//     TreeNode() {}
//
//     TreeNode(int val) {
//         this.val = val;
//     }
//
//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

class Solution {
    public void flatten(TreeNode root) {

        // Start from the root
        TreeNode current = root;

        // Process every node
        while (current != null) {

            // If there is no left subtree,
            // simply move to the right child
            if (current.left == null) {
                current = current.right;
                continue;
            }

            // Store the left subtree
            TreeNode leftSubtree = current.left;

            // Find the rightmost node
            // of the left subtree
            TreeNode predecessor = leftSubtree;

            while (predecessor.right != null) {
                predecessor = predecessor.right;
            }

            // Connect the original right subtree
            // after the left subtree
            predecessor.right = current.right;

            // Move the left subtree to the right
            current.right = current.left;

            // Remove the left pointer
            current.left = null;

            // Move to the next node
            current = current.right;
        }
    }
}


// 🎯 Interview Explanation
//
// I use an in-place approach to flatten the binary tree.
//
// The required order is preorder:
//
//     Root → Left → Right
//
// For every node, if it has a left subtree,
// I find the rightmost node of that left subtree.
//
// I connect the current node's original right subtree
// to that rightmost node.
//
// Then I move the left subtree to the right side
// and set the left pointer to null.
//
// This produces a linked-list-like structure
// using only the right pointers.
//
// Example:
//
// Before:
//
//        1
//       / \
//      2   5
//     / \   \
//    3   4   6
//
// After:
//
// 1 → 2 → 3 → 4 → 5 → 6
//
// Every node has:
//
//     left = null
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)
//
// No extra stack, list, or recursion is used.
//
//
// ⭐ Key Trick
//
// The most important part is finding the
// rightmost node of the left subtree.
//
//     predecessor = current.left
//
//     while (predecessor.right != null) {
//         predecessor = predecessor.right;
//     }
//
// Then connect:
//
//     predecessor.right = current.right;
//
// Move left subtree to right:
//
//     current.right = current.left;
//
// Remove left pointer:
//
//     current.left = null;
//
//
// Visual:
//
// Before:
//
//          current
//          /    \
//       left    right
//
//
// After:
//
//          current
//             \
//             left
//                \
//                 ...
//                   \
//                   right
//
//
// Final structure:
//
//     1 → 2 → 3 → 4 → 5 → 6
//
// left pointer of every node = null