// ---------- 💡 Logic ----------

// 1. Perform an inorder traversal.
//
// 2. First visit the left subtree.
//
// 3. Then visit the current/root node.
//
// 4. After visiting a node, decrease k.
//
// 5. If k == 0:
//       The current node is the kth smallest.
//
// 6. Then move to the right subtree.
//
// 7. Use a Stack to perform iterative inorder traversal.
//
//
// Important BST Property:
//
// Inorder Traversal:
// Left → Root → Right
//
// This gives the values in sorted order.


// ---------- 🔄 Algorithm ----------

// Step 1: Create an empty Stack<TreeNode>.
//
// Step 2: Set current = root.
//
// Step 3: While current is not null
//         OR stack is not empty:
//
//       a. Go to the leftmost node:
//
//          while current != null:
//              stack.push(current);
//              current = current.left;
//
//       b. Take the top node:
//
//          current = stack.pop();
//
//       c. Decrease k:
//
//          k--;
//
//       d. If k == 0:
//
//              return current.val;
//
//       e. Move to the right subtree:
//
//          current = current.right;


// ---------- 🧪 Dry Run ----------

// Input:
// root = [3,1,4,null,2]
// k = 1
//
// Tree:
//
//         3
//        / \
//       1   4
//        \
//         2
//
// --------------------------------
//
// stack = []
// current = 3
// k = 1
//
// --------------------------------
//
// Go left:
//
// Push 3:
//
// stack = [3]
//
// current = 1
//
// Push 1:
//
// stack = [3,1]
//
// current = null
//
// --------------------------------
//
// Pop:
//
// current = 1
// stack = [3]
//
// k = 1 - 1
//   = 0
//
// k == 0
//
// Therefore:
//
// return 1
//
// --------------------------------
//
// Final Answer:
//
// 1


// ---------- ☕ Java Code ----------

import java.util.*;

class Solution {
    public int kthSmallest(TreeNode root, int k) {

        Stack<TreeNode> stack = new Stack<>();

        TreeNode current = root;

        while (current != null || !stack.isEmpty()) {

            // Go to the leftmost node
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            // Visit the node
            current = stack.pop();

            // Count the visited node
            k--;

            // If this is the kth node
            if (k == 0) {
                return current.val;
            }

            // Move to the right subtree
            current = current.right;
        }

        return -1;
    }
}


// ---------- 🎯 Interview Explanation ----------

// I use the fact that inorder traversal of a BST
// gives values in sorted order.
//
// I perform inorder traversal iteratively using a Stack.
//
// Every time I visit a node, I decrease k by 1.
//
// When k becomes 0, the current node is the kth
// smallest value, so I return its value.
//
// Time Complexity:
// O(H + k)
//
// H = height of the BST.
//
// Space Complexity:
// O(H)
//
// for the stack.


// ---------- ⭐ Key Trick ----------

// BST Inorder Traversal:
//
// Left → Root → Right
//
//        ↓
//
// Sorted Order
//
//        ↓
//
// kth visited node
//        ↓
//
// kth smallest value
//
// Remember:
//
// k = 1 → smallest value
//
// k = 2 → second smallest
//
// k = 3 → third smallest