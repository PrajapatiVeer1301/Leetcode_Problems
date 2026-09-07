// 💡 Logic
//
// We will use BFS (Breadth First Search) for this problem.
//
// BFS traverses the N-ary tree level by level.
//
// We use a Queue to store the nodes that need to be processed.
//
// How it works:
//
// 1. If root is null, return an empty list.
// 2. Add the root node to the queue.
// 3. Find how many nodes are present in the current level.
// 4. Process exactly those nodes.
// 5. Add each node's value to the current level list.
// 6. Add all children of the current node to the queue.
// 7. Add the completed level to the result.
// 8. Repeat until the queue becomes empty.


// 🔄 Algorithm
//
// Queue = [root]
//
// while queue is not empty:
//
//     Find the number of nodes in the current level.
//
//     Create an empty list called level.
//
//     Process all nodes of the current level:
//
//         Remove one node from the queue.
//         Add node.val to level.
//         Add all children of the node to the queue.
//
//     Add level to result.
//
// Return result.


// 🧪 Dry Run
//
// Example:
//
//           1
//        /  |  \
//       3   2   4
//      / \
//     5   6
//
//
// Initially:
//
// Queue = [1]
// Result = []
//
//
// Level 1:
//
// Process node 1.
//
// Level = [1]
// Queue = [3, 2, 4]
//
// Result = [[1]]
//
//
// Level 2:
//
// Process nodes 3, 2, and 4.
//
// Level = [3, 2, 4]
//
// Node 3 has children 5 and 6.
//
// Queue = [5, 6]
//
// Result = [[1], [3, 2, 4]]
//
//
// Level 3:
//
// Process nodes 5 and 6.
//
// Level = [5, 6]
// Queue = []
//
// Result = [[1], [3, 2, 4], [5, 6]]
//
// The queue is now empty, so the traversal is complete.


// ⭐ Key Trick
//
// The most important trick is:
//
// int levelSize = queue.size();
//
// This tells us how many nodes belong to the current level.
//
// Then we process exactly that many nodes:
//
// for (int i = 0; i < levelSize; i++)
//
// This helps us keep every level in a separate list.


// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// Every node is visited exactly once.
//
// Space Complexity: O(n)
//
// In the worst case, the queue can contain O(n) nodes.


// 🧑‍💻 Java Code

import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(Node root) {

        // If the tree is empty, return an empty list
        if (root == null) {
            return new ArrayList<>();
        }

        // Create a queue for BFS traversal
        Queue<Node> queue = new LinkedList<>();

        // Add the root node to the queue
        queue.offer(root);

        // Store the final answer
        List<List<Integer>> result = new ArrayList<>();

        // Continue until the queue becomes empty
        while (!queue.isEmpty()) {

            // Get the number of nodes in the current level
            int levelSize = queue.size();

            // Store the values of the current level
            List<Integer> level = new ArrayList<>();

            // Process all nodes of the current level
            for (int i = 0; i < levelSize; i++) {

                // Remove one node from the queue
                Node node = queue.poll();

                // Add the node's value to the current level
                level.add(node.val);

                // Add all children of the current node to the queue
                for (Node child : node.children) {
                    queue.offer(child);
                }
            }

            // Add the current level to the final result
            result.add(level);
        }

        // Return the level order traversal
        return result;
    }
}


// ⭐ Most Important Line
//
// int levelSize = queue.size();
//
// It tells us how many nodes are present in the current level.
//
// For example:
//
// Queue = [3, 2, 4]
//
// levelSize = 3
//
// So we process exactly 3 nodes.
//
// Their children are added to the queue,
// but they will be processed in the NEXT level.