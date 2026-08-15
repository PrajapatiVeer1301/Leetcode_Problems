// We use Recursion and Divide & Conquer.
//
// 1. Traverse the expression and find every operator.
//
// 2. Treat each operator as a possible splitting point.
//
// 3. Split the expression into:
//       Left part
//       Right part
//
// 4. Recursively find all possible results
//    from the left and right parts.
//
// 5. Combine every left result with every right
//    result using the current operator.
//
// 6. If there is no operator, the expression is
//    simply a number, so return that number.


// Step 1: Create a recursive method solve(expression).
//
// Step 2: Create an ArrayList<Integer> result.
//
// Step 3: Traverse every character of expression.
//
// Step 4: If the character is '+', '-' or '*':
//
//         Split expression into left and right.
//
// Step 5: Recursively calculate:
//         leftResults
//         rightResults
//
// Step 6: Use nested loops to combine every
//         left result with every right result.
//
// Step 7: Apply the current operator.
//
// Step 8: If result is empty, expression contains
//         only a number. Convert it to integer.
//
// Step 9: Return result.

//----------- Dry Run ---------
// Input:
// expression = "2-1-1"
//
// First '-':
//
// Left  = "2"
// Right = "1-1"
//
// solve("2") → [2]
//
// solve("1-1"):
//
// Left  = "1"
// Right = "1"
//
// 1 - 1 = 0
//
// Therefore:
//
// 2 - 0 = 2
//
// Result = [2]
//
//
// --------------------------------
//
// Second '-' in "2-1-1":
//
// Left  = "2-1"
// Right = "1"
//
// solve("2-1"):
//
// 2 - 1 = 1
//
// solve("1") → [1]
//
// Therefore:
//
// 1 - 1 = 0
//
// Result = [2, 0]
//
// Final Output:
//
// [2, 0]
//
// Order does not matter, so [0, 2] is also correct.


import java.util.*;

class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < expression.length(); i++) {

            char ch = expression.charAt(i);

            if (ch == '+' || ch == '-' || ch == '*') {

                List<Integer> left =
                    diffWaysToCompute(expression.substring(0, i));

                List<Integer> right =
                    diffWaysToCompute(expression.substring(i + 1));

                for (int a : left) {
                    for (int b : right) {

                        if (ch == '+') {
                            result.add(a + b);
                        } 
                        else if (ch == '-') {
                            result.add(a - b);
                        } 
                        else {
                            result.add(a * b);
                        }
                    }
                }
            }
        }

        // No operator means it is a number
        if (result.isEmpty()) {
            result.add(Integer.parseInt(expression));
        }

        return result;
    }
}

// Input:
// expression = "2*3-4*5"
//
// Output:
// [-34, -14, -10, -10, 10]
//
// The order of the results does not matter.


//  ⭐ Key interview pattern

// Find Operator
//       ↓
// Split Left + Right
//       ↓
// Recursively solve both
//       ↓
// Combine all results
//       ↓
// Store in result