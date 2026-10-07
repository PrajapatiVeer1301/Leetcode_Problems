### 💡 Logic
### This problem uses BFS (Breadth-First Search).
###
### BFS traverses the binary tree level by level.
###
### For each level:
### 1. Find how many nodes are present in the current level.
### 2. Calculate the sum of all node values.
### 3. Calculate the average using:
###       average = sum / number_of_nodes
### 4. Add the average to the result list.
###
### ⭐ Key Trick
### The current size of the queue tells us how many nodes
### are present in the current level.
###
### level_size = len(queue)
###
### This allows us to process each level separately.


### 🔄 Algorithm
###
### 1. Create an empty queue.
###
### 2. Add the root node to the queue.
###
### 3. Continue while the queue is not empty.
###
### 4. Get the number of nodes in the current level:
###       level_size = len(queue)
###
### 5. Initialize level_sum = 0.
###
### 6. Process every node of the current level:
###       - Remove a node from the queue.
###       - Add its value to level_sum.
###       - Add its left child to the queue.
###       - Add its right child to the queue.
###
### 7. Calculate the average:
###       average = level_sum / level_size
###
### 8. Add the average to the result list.
###
### 9. Return the result list.


### 🧑‍💻 Python Code

from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        ### Queue is used for BFS traversal
        queue = deque([root])

        ### Store the average of every level
        result = []

        ### Process the tree level by level
        while queue:

            ### Number of nodes in the current level
            level_size = len(queue)

            ### Store the sum of values of the current level
            level_sum = 0

            ### Process all nodes of the current level
            for _ in range(level_size):

                ### Remove a node from the queue
                node = queue.popleft()

                ### Add the node value to the level sum
                level_sum += node.val

                ### Add the left child to the queue
                if node.left:
                    queue.append(node.left)

                ### Add the right child to the queue
                if node.right:
                    queue.append(node.right)

            ### Calculate the average of the current level
            average = level_sum / level_size

            ### Add the average to the result
            result.append(average)

        ### Return the averages of all levels
        return result


### 🧪 Dry Run
###
### Example:
### root = [3,9,20,null,null,15,7]
###
### Tree:
###
###         3
###        / \
###       9   20
###          /  \
###         15   7
###
###
### Level 0:
###
### queue = [3]
### level_size = 1
### level_sum = 3
###
### average = 3 / 1 = 3.0
###
### result = [3.0]
###
###
### Level 1:
###
### queue = [9, 20]
### level_size = 2
### level_sum = 9 + 20 = 29
###
### average = 29 / 2 = 14.5
###
### result = [3.0, 14.5]
###
###
### Level 2:
###
### queue = [15, 7]
### level_size = 2
### level_sum = 15 + 7 = 22
###
### average = 22 / 2 = 11.0
###
### Final result:
### [3.0, 14.5, 11.0]


### 🎯 Interview Explanation
###
### "I use BFS to traverse the binary tree level by level.
### For each level, I use the queue size to find the number
### of nodes in that level.
### Then I calculate the sum of all node values and divide
### it by the number of nodes to get the average.
### Finally, I add each average to the result list."


### ⭐ Key Trick
###
### The important trick is:
###
### level_size = len(queue)
###
### It gives the exact number of nodes in the current level.
###
### We process exactly these nodes before moving to the next level.


### ⏱️ Complexity
###
### Time Complexity: O(n)
### Every node is visited exactly once.
###
### Space Complexity: O(n)
### The queue can contain up to O(n) nodes in the worst case.