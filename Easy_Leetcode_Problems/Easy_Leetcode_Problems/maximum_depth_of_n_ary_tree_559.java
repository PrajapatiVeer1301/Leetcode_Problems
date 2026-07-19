// Logic:
//
// 1. If the root is null,
//    return 0.
//
// 2. Find the maximum depth
//    among all child nodes.
//
// 3. Add 1 for the current node.
//
// 4. Return the maximum depth.

// Algorithm:
//
// 1. Check if the root is null.
//    If yes, return 0.
//
// 2. Initialize maxDepth = 0.
//
// 3. Traverse all children of the root.
//
// 4. Recursively find the depth
//    of each child.
//
// 5. Store the maximum depth.
//
// 6. Return maxDepth + 1.

class Solution {
    public int maxDepth(Node root) {

        if (root == null) {
            return 0;
        }

        int max = 0;

        for (Node child : root.children) {
            max = Math.max(max, maxDepth(child));
        }

        return max + 1;
    }
}

// Interview Explanation:
//
// 1. I used a recursive DFS approach.
//
// 2. If the current node is null,
//    I return 0.
//
// 3. Otherwise, I recursively calculate
//    the depth of each child.
//
// 4. I keep track of the maximum depth
//    among all children.
//
// 5. Finally, I add 1 for the current node
//    and return the result.
//
// Time Complexity: O(n)
// Space Complexity: O(h)
//
// where:
// n = number of nodes
// h = height of the tree