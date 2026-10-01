// ⭐ MAIN LOGIC
//
// We use a Stack to check whether the brackets are valid.
//
// - If we find an opening bracket, push it into the stack.
// - If we find a closing bracket, compare it with the
//   top element of the stack.
// - If they do not match, return false.
// - After processing the complete string, if the stack is empty,
//   return true.
//
//
// Example:
//
// s = "([])"
//
// Processing:
//
// ( → push
// [ → push
// ] → matches [ → pop
// ) → matches ( → pop
//
// Stack is empty, so the answer is:
//
// true
//
//
// 🔄 ALGORITHM
//
// 1. Create an empty stack.
//
// 2. Traverse every character of the string.
//
// 3. If the character is an opening bracket:
//
//       '(' or '[' or '{'
//
//    Push it into the stack.
//
// 4. If the character is a closing bracket:
//
//       ')' or ']' or '}'
//
//    Check whether the stack is empty.
//
//    If the stack is empty:
//        Return false.
//
// 5. Check whether the top element of the stack
//    matches the current closing bracket.
//
//    If it does not match:
//        Return false.
//
// 6. If it matches:
//       Pop the opening bracket from the stack.
//
// 7. After processing all characters:
//
//       If stack is empty:
//           Return true
//
//       Otherwise:
//           Return false.
//
//
// 🧑‍💻 JAVA CODE

import java.util.*;

class Solution {
    public boolean isValid(String s) {

        // Stack to store opening brackets
        Stack<Character> stack = new Stack<>();

        // Traverse every character
        for (char ch : s.toCharArray()) {

            // If it is an opening bracket
            if (ch == '(' || ch == '[' || ch == '{') {

                // Push the opening bracket into the stack
                stack.push(ch);

            } else {

                // If stack is empty, there is no
                // corresponding opening bracket
                if (stack.isEmpty()) {
                    return false;
                }

                // Get the top opening bracket
                char top = stack.peek();

                // Check if the brackets match
                if ((ch == ')' && top != '(') ||
                    (ch == ']' && top != '[') ||
                    (ch == '}' && top != '{')) {

                    return false;
                }

                // Remove the matched opening bracket
                stack.pop();
            }
        }

        // The string is valid only if
        // no opening brackets are left
        return stack.isEmpty();
    }
}


// 🧪 DRY RUN
//
// Example:
//
// s = "([)]"
//
//
// Step 1:
//
// Character = '('
//
// Opening bracket → push
//
// stack = ['(']
//
//
// Step 2:
//
// Character = '['
//
// Opening bracket → push
//
// stack = ['(', '[']
//
//
// Step 3:
//
// Character = ')'
//
// Expected opening bracket:
//
// '('
//
// But stack top is:
//
// '['
//
// '[' != '('
//
// Therefore:
//
// return false
//
//
// Final Answer:
//
// false
//
//
// 🧪 ANOTHER EXAMPLE
//
// s = "()[]{}"
//
// Processing:
//
// ( → push
// ) → matches ( → pop
//
// [ → push
// ] → matches [ → pop
//
// { → push
// } → matches { → pop
//
//
// Final stack:
//
// []
//
// Therefore:
//
// true
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I use a stack to validate the brackets.
// Whenever I encounter an opening bracket, I push it
// onto the stack.
//
// For a closing bracket, I first check whether the stack
// is empty and then compare it with the top opening bracket.
// If they do not match, I return false.
//
// If they match, I remove the opening bracket from the stack.
//
// After processing the entire string, the string is valid
// only when the stack is empty."
//
//
// ⏱️ COMPLEXITY
//
// Time Complexity: O(n)
//
// Each character is processed exactly once.
//
// Space Complexity: O(n)
//
// In the worst case, all characters can be opening brackets,
// so the stack can contain n elements.