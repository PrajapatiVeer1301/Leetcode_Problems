// ### 💡 Logic
// ### This problem uses BFS (Breadth-First Search).
// ###
// ### BFS traverses the binary tree level by level.
// ###
// ### For each level:
// ### 1. Find how many nodes are present in the current level.
// ### 2. Calculate the sum of all node values.
// ### 3. Calculate the average using:
// ###       average = sum / number_of_nodes
// ### 4. Add the average to the result list.
// ###
// ### ⭐ Key Trick
// ### The current size of the queue tells us how many nodes
// ### are present in the current level.
// ###
// ### levelSize = queue.size();
// ###
// ### This allows us to process each level separately.


// ### 🔄 Algorithm
// ###
// ### 1. Create an empty queue.
// ###
// ### 2. Add the root node to the queue.
// ###
// ### 3. Continue while the queue is not empty.
// ###
// ### 4. Get the number of nodes in the current level:
// ###       levelSize = queue.size();
// ###
// ### 5. Initialize levelSum = 0.
// ###
// ### 6. Process every node of the current level:
// ###       - Remove a node from the queue.
// ###       - Add its value to levelSum.
// ###       - Add its left child to the queue.
// ###       - Add its right child to the queue.
// ###
// ### 7. Calculate the average:
// ###       average = levelSum / levelSize;
// ###
// ### 8. Add the average to the result list.
// ###
// ### 9. Return the result list.


// ### 🧑‍💻 Java Code

import java.util.*;

class Solution {
    
    public List<Double> averageOfLevels(TreeNode root) {
        
        // ### Queue is used for BFS traversal
        Queue<TreeNode> queue = new LinkedList<>();
        
        // ### Add the root node to the queue
        queue.offer(root);
        
        // ### Store the average of every level
        List<Double> result = new ArrayList<>();
        
        // ### Process the tree level by level
        while (!queue.isEmpty()) {
            
            // ### Number of nodes in the current level
            int levelSize = queue.size();
            
            // ### Store the sum of values of the current level
            double levelSum = 0;
            
            // ### Process all nodes of the current level
            for (int i = 0; i < levelSize; i++) {
                
                // ### Remove a node from the queue
                TreeNode node = queue.poll();
                
                // ### Add the node value to the level sum
                levelSum += node.val;
                
                // ### Add the left child to the queue
                if (node.left != null) {
                    queue.offer(node.left);
                }
                
                // ### Add the right child to the queue
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            
            // ### Calculate the average of the current level
            double average = levelSum / levelSize;
            
            // ### Add the average to the result
            result.add(average);
        }
        
        // ### Return the averages of all levels
        return result;
    }
}


// ### 🧪 Dry Run
// ###
// ### Example:
// ### root = [3,9,20,null,null,15,7]
// ###
// ### Tree:
// ###
// ###         3
// ###        / \
// ###       9   20
// ###          /  \
// ###         15   7
// ###
// ### Level 0:
// ###
// ### queue = [3]
// ### levelSize = 1
// ### levelSum = 3
// ###
// ### average = 3 / 1 = 3.0
// ###
// ### result = [3.0]
// ###
// ###
// ### Level 1:
// ###
// ### queue = [9, 20]
// ### levelSize = 2
// ### levelSum = 9 + 20 = 29
// ###
// ### average = 29 / 2 = 14.5
// ###
// ### result = [3.0, 14.5]
// ###
// ###
// ### Level 2:
// ###
// ### queue = [15, 7]
// ### levelSize = 2
// ### levelSum = 15 + 7 = 22
// ###
// ### average = 22 / 2 = 11.0
// ###
// ### Final result:
// ### [3.0, 14.5, 11.0]


// ### 🎯 Interview Explanation
// ###
// ### "I use BFS to traverse the binary tree level by level.
// ### For each level, I use the queue size to find the number
// ### of nodes in that level.
// ### Then I calculate the sum of all node values and divide
// ### it by the number of nodes to get the average.
// ### Finally, I add each average to the result list."


// ### ⭐ Key Trick
// ###
// ### The important trick is:
// ###
// ### int levelSize = queue.size();
// ###
// ### It gives the exact number of nodes in the current level.
// ###
// ### We process exactly these nodes before moving to the next level.


// ### ⏱️ Complexity
// ###
// ### Time Complexity: O(n)
// ### Every node is visited exactly once.
// ###
// ### Space Complexity: O(n)
// ### The queue can contain up to O(n) nodes in the worst case.