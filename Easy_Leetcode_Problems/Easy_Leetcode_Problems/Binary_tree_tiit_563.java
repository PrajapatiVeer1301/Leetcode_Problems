// 🔥 Main Logic
//
// We will use Postorder DFS for this problem.
//
// Postorder means:
//
// Left → Right → Root
//
// To calculate the tilt of a node, we first need:
//
// - The sum of the left subtree
// - The sum of the right subtree
//
// Therefore, we first calculate the sums of both subtrees
// and then calculate the tilt of the current node.
//
// The DFS function will return the total sum of the current subtree.
//
// At the same time, we will add every node's tilt to totalTilt.


// 🔄 Algorithm
//
// 1. Initialize totalTilt = 0.
//
// 2. Create a DFS function.
//
// 3. If the current node is null:
//       return 0
//
// 4. Recursively find the sum of the left subtree.
//
// 5. Recursively find the sum of the right subtree.
//
// 6. Calculate the current node's tilt:
//
//       Math.abs(leftSum - rightSum)
//
// 7. Add this tilt to totalTilt.
//
// 8. Return the sum of the current subtree:
//
//       leftSum + rightSum + node.val
//
// 9. Call DFS starting from the root.
//
// 10. Return totalTilt.


// 🧪 Dry Run
//
// Example:
//
//        4
//       / \
//      2   9
//     / \   \
//    3   5   7
//
//
// Node 3:
//
// Left = 0
// Right = 0
//
// Tilt = |0 - 0| = 0
//
// Subtree Sum = 3
//
//
// Node 5:
//
// Left = 0
// Right = 0
//
// Tilt = |0 - 0| = 0
//
// Subtree Sum = 5
//
//
// Node 2:
//
// Left subtree sum = 3
// Right subtree sum = 5
//
// Tilt = |3 - 5| = 2
//
// Subtree Sum:
//
// 3 + 2 + 5 = 10
//
//
// Node 7:
//
// Left = 0
// Right = 0
//
// Tilt = 0
//
// Subtree Sum = 7
//
//
// Node 9:
//
// Left subtree sum = 0
// Right subtree sum = 7
//
// Tilt = |0 - 7| = 7
//
// Subtree Sum:
//
// 0 + 9 + 7 = 16
//
//
// Node 4:
//
// Left subtree sum = 10
// Right subtree sum = 16
//
// Tilt = |10 - 16| = 6
//
//
// Final Total Tilt:
//
// 0 + 0 + 2 + 0 + 7 + 6 = 15
//
// Answer = 15


// 🎯 Interview Explanation
//
// "I will use postorder DFS because the tilt of a node depends
// on the sums of its left and right subtrees.
//
// Therefore, I first calculate the left and right subtree sums.
//
// My DFS function returns the total sum of the current subtree.
//
// After getting both subtree sums, I calculate:
//
// Math.abs(leftSum - rightSum)
//
// and add it to totalTilt.
//
// Then I return:
//
// leftSum + rightSum + node.val
//
// This allows the parent node to get its subtree sum without
// recalculating the entire subtree.
//
// Finally, I return totalTilt."


// ⭐ Key Trick
//
// The most important trick is that the DFS function returns
// the subtree sum.
//
// We calculate the tilt separately:
//
// totalTilt += Math.abs(leftSum - rightSum);
//
// And return the subtree sum:
//
// return leftSum + rightSum + node.val;
//
// This means every node is visited only once.
//
// We do not calculate the subtree sum again and again.


// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// Every node is visited exactly once.
//
//
// Space Complexity: O(h)
//
// The recursion stack uses O(h) space,
// where h is the height of the tree.
//
// In the worst case, the tree can be completely skewed,
// so h can be n.
//
// Therefore, worst-case space complexity is O(n).


// 🧑‍💻 Java Code

// Definition for a binary tree node.
// public class TreeNode {
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

    // Store the total tilt of all nodes
    private int totalTilt = 0;

    public int findTilt(TreeNode root) {

        // Start DFS from the root
        dfs(root);

        // Return the total tilt
        return totalTilt;
    }

    // DFS returns the sum of the current subtree
    private int dfs(TreeNode node) {

        // If the node is null, its subtree sum is 0
        if (node == null) {
            return 0;
        }

        // Find the sum of the left subtree
        int leftSum = dfs(node.left);

        // Find the sum of the right subtree
        int rightSum = dfs(node.right);

        // Calculate the tilt of the current node
        int tilt = Math.abs(leftSum - rightSum);

        // Add the current node's tilt to the total
        totalTilt += tilt;

        // Return the sum of the current subtree
        return leftSum + rightSum + node.val;
    }
}