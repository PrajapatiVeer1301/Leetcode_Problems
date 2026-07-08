// Logic:
//
// 1. If the current node is null,
//    return null.
//
// 2. If the current node's value equals val,
//    return the current node.
//
// 3. If val is smaller than the current node's value,
//    search the left subtree.
//
// 4. Otherwise,
//    search the right subtree.
//
// 5. Return the result.

// Algorithm:
//
// 1. Start searching from the root node.
//
// 2. If the root is null,
//    return null.
//
// 3. If root.val == val,
//    return root.
//
// 4. If val < root.val,
//    recursively search the left subtree.
//
// 5. Otherwise,
//    recursively search the right subtree.
//
// 6. Return the found node or null.

class Solution {
    public TreeNode searchBST(TreeNode root, int val) {

        if (root == null) {
            return null;
        }

        if (root.val == val) {
            return root;
        }

        if (val < root.val) {
            return searchBST(root.left, val);
        }

        return searchBST(root.right, val);
    }
}

// Interview Explanation:
//
// 1. Since it is a Binary Search Tree,
//    I compare the target value with the current node.
//
// 2. If the values are equal,
//    I return the current node.
//
// 3. If the target value is smaller,
//    I search only the left subtree.
//
// 4. If the target value is greater,
//    I search only the right subtree.
//
// 5. This avoids searching the entire tree
//    because of the BST property.
//
// Time Complexity: O(h)
// Space Complexity: O(h)
//
// where h is the height of the tree.