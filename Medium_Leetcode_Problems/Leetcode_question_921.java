// 💡 LOGIC
//
// We need to find the minimum number of parentheses
// that must be inserted to make the given string valid.
//
// We will use two variables:
//
// balance → Number of unmatched opening '(' brackets.
// answer  → Number of parentheses that we need to insert.
//
//
//
// When we find '(':
//
//     balance++;
//
// Because we have one more opening bracket.
//
//
//
// When we find ')':
//
// If balance > 0:
//
//     balance--;
//
// This means the ')' can match with an existing '('.
//
// If balance == 0:
//
//     answer++;
//
// There is no opening '(' available to match this ')',
// so we need to insert one '(' before it.
//
//
//
// After processing the complete string:
//
// If some '(' brackets are still unmatched,
// we need one ')' for each of them.
//
// Therefore:
//
//     answer += balance;
//
//
//
// ⭐ KEY TRICK
//
// The minimum number of insertions is:
//
//     answer = unmatched ')' + unmatched '('
//
// We do not need a stack.
// We only need to keep track of the balance.
//
//
// 🔄 ALGORITHM
//
// 1. Initialize:
//       balance = 0
//       answer = 0
//
// 2. Traverse every character of the string.
//
// 3. If the character is '(':
//       Increase balance.
//
// 4. If the character is ')':
//
//       If balance > 0:
//           Decrease balance.
//
//       Otherwise:
//           Increase answer.
//           This means we need to insert '('.
//
// 5. After traversing the string:
//       Add the remaining balance to answer.
//
// 6. Return answer.
//
//
// 🧑‍💻 JAVA CODE

class Solution {
    public int minAddToMakeValid(String s) {

        // Store the number of unmatched opening brackets
        int balance = 0;

        // Store the number of brackets that need to be inserted
        int answer = 0;

        // Traverse every character of the string
        for (char ch : s.toCharArray()) {

            // If it is an opening bracket
            if (ch == '(') {

                // Increase the number of unmatched '('
                balance++;

            } else {

                // If an opening bracket is available
                if (balance > 0) {

                    // Match the ')' with an existing '('
                    balance--;

                } else {

                    // No '(' is available.
                    // We need to insert one '('.
                    answer++;
                }
            }
        }

        // Any remaining '(' needs a corresponding ')'
        answer += balance;

        // Return the minimum number of insertions
        return answer;
    }
}


// 🧪 DRY RUN
//
// Example 1:
//
// s = "())"
//
// Initially:
//
// balance = 0
// answer = 0
//
//
//
// Character '(':
//
// balance = 1
//
//
//
// Character ')':
//
// balance > 0
//
// balance = 0
//
//
//
// Character ')':
//
// balance == 0
//
// No '(' is available.
//
// answer = 1
//
//
//
// End:
//
// balance = 0
// answer = 1
//
// Therefore:
//
// Output = 1
//
//
//
// Example 2:
//
// s = "((("
//
// Initially:
//
// balance = 0
// answer = 0
//
//
//
// First '(':
//
// balance = 1
//
// Second '(':
//
// balance = 2
//
// Third '(':
//
// balance = 3
//
//
//
// End:
//
// balance = 3
// answer = 0
//
// There are 3 unmatched '(' brackets.
//
// We need 3 ')' brackets.
//
// answer = answer + balance
//
// answer = 0 + 3
// answer = 3
//
// Therefore:
//
// Output = 3
//
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I use a balance counter to track unmatched opening
// parentheses. Whenever I see an opening parenthesis,
// I increase the balance.
//
// When I see a closing parenthesis, if there is an
// unmatched opening parenthesis, I decrease the balance.
//
// Otherwise, there is no opening parenthesis available
// to match the closing parenthesis, so I need to insert
// one opening parenthesis and increase the answer.
//
// After processing the entire string, any remaining
// unmatched opening parentheses need closing parentheses.
// Therefore, I add the remaining balance to the answer.
//
// This gives the minimum number of insertions without
// using a stack."
//
//
//
// ⏱️ COMPLEXITY
//
// Time Complexity: O(n)
//
// We traverse the string only once.
//
// Space Complexity: O(1)
//
// We use only two variables:
//     balance
//     answer
//
//
//
// ⭐ IMPORTANT POINT
//
// We do not need to actually insert the brackets.
// We only count how many insertions are required.
//
//
//
// Formula:
//
//     Minimum Insertions
//     = Unmatched ')' + Unmatched '('