//------ 💡 Logic -------

// 1. Create an empty result list.
//
// 2. If root is null, return an empty list.
//
// 3. Create a Stack and add root.
//
// 4. While stack is not empty:
//
//       node = stack.pop()
//
//       Add node.val to result.
//
// 5. Push children from RIGHT to LEFT.
//
// 6. Because Stack follows LIFO,
//    the LEFT child will be processed first.
//
// 7. Return result.

// ----- 🔄 Algorithm ------

// Step 1: Create result = new ArrayList<>().
//
// Step 2: If root == null, return result.
//
// Step 3: Create Stack<Node> stack.
//
// Step 4: Push root into stack.
//
// Step 5: While stack is not empty:
//
//       node = stack.pop();
//
//       result.add(node.val);
//
// Step 6: Traverse children from right to left
//         and push them into stack.
//
// Step 7: Return result.

//-------- 🧪 Dry Run -------
// Input:
// root = [1,null,3,2,4,null,5,6]
//
// Tree:
//
//         1
//       / | \
//      3  2  4
//     / \
//    5   6
//
// --------------------------------
//
// Initial:
//
// stack = [1]
// result = []
//
// --------------------------------
//
// Pop 1
//
// result = [1]
//
// Children = [3,2,4]
//
// Push right-to-left:
//
// stack = [4,2,3]
//
// --------------------------------
//
// Pop 3
//
// result = [1,3]
//
// Children = [5,6]
//
// Push right-to-left:
//
// stack = [4,2,6,5]
//
// --------------------------------
//
// Pop 5
//
// result = [1,3,5]
//
// --------------------------------
//
// Pop 6
//
// result = [1,3,5,6]
//
// --------------------------------
//
// Pop 2
//
// result = [1,3,5,6,2]
//
// --------------------------------
//
// Pop 4
//
// result = [1,3,5,6,2,4]
//
// --------------------------------
//
// Stack is empty.
//
// Final Output:
//
// [1,3,5,6,2,4]


import java.util.*;

class Solution {
    public List<Integer> preorder(Node root) {

        List<Integer> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {

            Node node = stack.pop();

            result.add(node.val);

            // Push children from right to left
            for (int i = node.children.size() - 1; i >= 0; i--) {
                stack.push(node.children.get(i));
            }
        }

        return result;
    }
}

//------- 🎯 Interview Explanation ---------

// I used an iterative approach with a Stack.
//
// First, I push the root into the stack.
//
// Then I repeatedly pop a node, add its value
// to the result, and push all its children.
//
// Since Stack follows LIFO order, I push the
// children from right to left.
//
// Therefore, the leftmost child is processed first,
// giving the required preorder traversal.
//
// Preorder:
// Root → Children from left to right
//
// Time Complexity: O(n)
//
// Space Complexity: O(n)
//
// where n is the number of nodes.

//======  ⭐ Key Trick ------
// Push children RIGHT → LEFT
//
// Stack:
// [4, 2, 3]
//
// Pop:
// 3 first
//
// Therefore traversal becomes:
// LEFT → RIGHT