// Logic:
//
// 1. Use BFS (Level Order Traversal).
//
// 2. Process the binary tree level by level.
//
// 3. For every level, find the last node.
//
// 4. The last node of each level is
//    visible from the right side.
//
// 5. Add that node's value to result.
//
// Example:
//
//        1
//       / \
//      2   3
//       \   \
//        5   4
//
// Level 0 → [1]     → 1
// Level 1 → [2,3]   → 3
// Level 2 → [5,4]   → 4
//
// Answer = [1,3,4]

// Algorithm:
//
// 1. If root == null, return empty list.
//
// 2. Create a Queue and add root.
//
// 3. While queue is not empty:
//
//      Find the size of current level.
//
// 4. Process every node of that level.
//
// 5. If current node is the last node
//    of the level:
//
//      Add node.val to result.
//
// 6. Add left and right children
//    to the queue.
//
// 7. Return result.

// Dry Run:
//
// Input:
//
// root = [1,2,3,null,5,null,4]
//
// Tree:
//
//        1
//       / \
//      2   3
//       \   \
//        5   4
//
// -------------------------
//
// Level 0:
//
// queue = [1]
// levelSize = 1
//
// node = 1
// i = 0
//
// i == levelSize - 1
// 0 == 0 → true
//
// result = [1]
//
// Add 2 and 3
//
// queue = [2,3]
//
// -------------------------
//
// Level 1:
//
// queue = [2,3]
// levelSize = 2
//
// node = 2
// i = 0
//
// 0 == 1 → false
//
// Add 5
//
// node = 3
// i = 1
//
// 1 == 1 → true
//
// result = [1,3]
//
// Add 4
//
// queue = [5,4]
//
// -------------------------
//
// Level 2:
//
// queue = [5,4]
// levelSize = 2
//
// node = 5
// i = 0
//
// 0 == 1 → false
//
// node = 4
// i = 1
//
// 1 == 1 → true
//
// result = [1,3,4]
//
// -------------------------
//
// Final Answer:
//
// [1,3,4]

import java.util.*;

class Solution {

    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {

            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {

                TreeNode node = queue.poll();

                if (i == levelSize - 1) {
                    result.add(node.val);
                }

                if (node.left != null) {
                    queue.offer(node.left);
                }

                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }

        return result;
    }
}


// Interview Explanation:
//
// I used BFS, or level-order traversal,
// to process the binary tree level by level.
//
// For every level, I store its size.
// While traversing that level,
// the last node is the rightmost node.
//
// Therefore, when:
//
// i == levelSize - 1
//
// I add that node's value to the result.
//
// Finally, I return the result.
//
// Time Complexity: O(n)
//
// Space Complexity: O(n)


//  ⭐ Important Line
if (i == levelSize - 1) {
    result.add(node.val);
}