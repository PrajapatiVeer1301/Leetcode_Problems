// 💡 Logic
//
// We use two variables:
//
// depth     → stores the current nesting depth
// maxDepth  → stores the maximum nesting depth found
//
// When we find '(':
//     depth increases by 1.
//
// When we find ')':
//     depth decreases by 1.
//
// Every time depth increases, we update maxDepth.
//
// The maximum value of depth is the answer.
//
//
// 🔄 Algorithm
//
// 1. Initialize depth = 0.
//
// 2. Initialize maxDepth = 0.
//
// 3. Traverse every character of the string.
//
// 4. If the character is '(':
//      Increase depth by 1.
//      Update maxDepth.
//
// 5. If the character is ')':
//      Decrease depth by 1.
//
// 6. Return maxDepth.
//
//
// 🧑‍💻 Java Code

class Solution {
    public int maxDepth(String s) {

        // Store the current nesting depth
        int depth = 0;

        // Store the maximum nesting depth
        int maxDepth = 0;

        // Traverse every character in the string
        for (char ch : s.toCharArray()) {

            // If an opening parenthesis is found
            if (ch == '(') {

                // Increase the current depth
                depth++;

                // Update the maximum depth
                maxDepth = Math.max(maxDepth, depth);
            }

            // If a closing parenthesis is found
            else if (ch == ')') {

                // Decrease the current depth
                depth--;
            }
        }

        // Return the maximum nesting depth
        return maxDepth;
    }
}


// 🧪 Dry Run
//
// For:
//
// s = "(1)+((2))+(((3)))"
//
// Processing:
//
// ( → depth = 1 → maxDepth = 1
// ) → depth = 0
//
// ( → depth = 1
// ( → depth = 2 → maxDepth = 2
// ) → depth = 1
// ) → depth = 0
//
// ( → depth = 1
// ( → depth = 2
// ( → depth = 3 → maxDepth = 3
// ) → depth = 2
// ) → depth = 1
// ) → depth = 0
//
// Final:
//
// maxDepth = 3
//
// Answer = 3


// 🎯 Interview Explanation
//
// "I use a counter to track the current nesting depth.
// Whenever I encounter an opening parenthesis, I increase
// the depth and update the maximum depth.
// Whenever I encounter a closing parenthesis, I decrease
// the depth.
// The maximum value reached by the depth counter is the
// maximum nesting depth of the parentheses."


// ⏱️ Complexity
//
// Time Complexity: O(n)
// We traverse the string once.
//
// Space Complexity: O(1)
// We only use two integer variables.