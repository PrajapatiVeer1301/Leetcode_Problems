
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode increasingBST(TreeNode root) {

        // ## LOGIC:
        // In-order traversal gives BST values in sorted order.
        // Create a new tree using only right pointers.
        // Every node will have left = null.

        // Store values in sorted order.
        List<Integer> values = new ArrayList<>();

        // Perform in-order traversal.
        inorder(root, values);

        // Create a dummy node to build the new tree.
        TreeNode dummy = new TreeNode(0);
        TreeNode current = dummy;

        // Connect nodes using only right pointers.
        for (int value : values) {
            current.right = new TreeNode(value);
            current = current.right;
        }

        // Return the new root, skipping the dummy node.
        return dummy.right;
    }

    // In-order traversal: Left -> Root -> Right.
    private void inorder(TreeNode node, List<Integer> values) {
        if (node == null) {
            return;
        }

        inorder(node.left, values);
        values.add(node.val);
        inorder(node.right, values);
    }
}

/*
## EXAMPLE:
Input: root = [5, 1, 7]
Output: [1, null, 5, null, 7]

## DRY RUN:
Step 1: In-order traversal.
values = [1, 5, 7]

Step 2: Create the new tree.
1 -> 5 -> 7

Step 3: All left pointers are null.

Final tree:
1
 \
  5
   \
    7

## ALGORITHM:
1. Perform in-order traversal of the BST.
2. Store node values in a list.
3. Create a dummy node.
4. Create a new node for every value.
5. Connect each node using the right pointer.
6. Return dummy.right.

## INTERVIEW EXPLANATION:
In-order traversal of a BST gives values in sorted order.
I store the values and create a new tree in which every
node has a null left pointer and the next node is connected
through the right pointer.

## KEY TRICK:
In-order traversal = Left -> Root -> Right.
dummy.right gives the actual root of the new tree.

## TIME COMPLEXITY:
O(n), because every node is visited once.

## SPACE COMPLEXITY:
O(n), for the values list and the new tree.
*/
