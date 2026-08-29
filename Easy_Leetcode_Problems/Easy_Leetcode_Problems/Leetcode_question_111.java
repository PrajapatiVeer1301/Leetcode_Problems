// 💡 Logic
//
// We use BFS (Breadth First Search) to find the minimum depth.
//
// BFS visits the binary tree level by level.
//
// The first leaf node we find will always be
// the nearest leaf node from the root.
//
// We store two things in the queue:
//
//     (node, depth)
//
// node  → current tree node
// depth → depth of that node
//
// If the current node has no left child
// and no right child, it is a leaf node.
//
// Therefore, we immediately return its depth.


// 🔄 Algorithm
//
// Step 1: If root is null:
//         return 0.
//
// Step 2: Create a Queue.
//
// Step 3: Add root and its depth:
//
//         queue.add(new Pair(root, 1))
//
// Step 4: While the queue is not empty:
//
//         Remove the first node and its depth.
//
// Step 5: Check whether the current node is a leaf.
//
//         If:
//             node.left == null
//             AND
//             node.right == null
//
//         Then return depth.
//
// Step 6: If left child exists:
//
//         Add left child to the queue
//         with depth + 1.
//
// Step 7: If right child exists:
//
//         Add right child to the queue
//         with depth + 1.
//
// Step 8: Continue until the first leaf node is found.
//
// Step 9: Return the depth of the first leaf.


// 🧪 Dry Run
//
// Input:
//
// root = [3,9,20,null,null,15,7]
//
// Tree:
//
//         3
//        / \
//       9   20
//          /  \
//         15   7
//
// --------------------------------
//
// Initial:
//
// queue = [(3,1)]
//
// --------------------------------
//
// Level 1:
//
// Remove:
//
// node = 3
// depth = 1
//
// 3 is not a leaf because
// it has left and right children.
//
// Add its children:
//
// queue = [(9,2), (20,2)]
//
// --------------------------------
//
// Level 2:
//
// Remove:
//
// node = 9
// depth = 2
//
// 9 has:
//
// left = null
// right = null
//
// Therefore, 9 is a leaf.
//
// Return:
//
// depth = 2
//
// --------------------------------
//
// Final Answer:
//
// 2


// ☕ Java Code

import java.util.*;

class Solution {

    public int minDepth(TreeNode root) {

        // If tree is empty
        if (root == null) {
            return 0;
        }

        // Queue stores:
        // node and its depth
        Queue<Pair> queue = new LinkedList<>();

        // Add root with depth 1
        queue.offer(new Pair(root, 1));

        while (!queue.isEmpty()) {

            // Remove the first node
            Pair current = queue.poll();

            TreeNode node = current.node;
            int depth = current.depth;

            // Check if current node is a leaf
            if (node.left == null && node.right == null) {
                return depth;
            }

            // Add left child if it exists
            if (node.left != null) {
                queue.offer(new Pair(node.left, depth + 1));
            }

            // Add right child if it exists
            if (node.right != null) {
                queue.offer(new Pair(node.right, depth + 1));
            }
        }

        return 0;
    }

    // Helper class to store node and depth
    class Pair {

        TreeNode node;
        int depth;

        Pair(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}


// 🎯 Interview Explanation
//
// I use BFS to find the minimum depth of the binary tree.
//
// BFS visits nodes level by level.
//
// Because of this, the first leaf node found by BFS
// will always be the nearest leaf from the root.
//
// I store each node together with its depth in a queue.
//
// When I find a node with no left and right children,
// it is a leaf node, so I immediately return its depth.
//
// Time Complexity: O(n)
//
// In the worst case, we may visit all nodes.
//
// Space Complexity: O(n)
//
// In the worst case, the queue can contain O(n) nodes.


// ⭐ Key Trick
//
// Binary Tree:
//
//         Root
//        /    \
//       ↓      ↓
//    Level 2  Level 2
//       ↓
//    Level 3
//
// BFS
//   ↓
// Visit level by level
//   ↓
// Find first leaf
//   ↓
// Return its depth
//   ↓
// Minimum Depth
//
//
// ⭐ Remember:
//
// Leaf Node =
// left == null AND right == null
//
// BFS → Minimum Depth