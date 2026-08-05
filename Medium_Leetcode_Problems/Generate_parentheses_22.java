// Logic:
//
// 1. Use Backtracking.
//
// 2. Keep track of:
//      Current String
//      Open Brackets
//      Close Brackets
//
// 3. Add '(' if open < n.
//
// 4. Add ')' only if
//    close < open.
//
// 5. When the string length
//    becomes 2*n,
//    store it.
//
// 6. Return all combinations.

// Algorithm:
//
// 1. Create an empty answer list.
//
// 2. Start recursion with:
//
//      current = ""
//      open = 0
//      close = 0
//
// 3. If open < n,
//    add '('.
//
// 4. If close < open,
//    add ')'.
//
// 5. If current length == 2*n,
//    add current to answer.
//
// 6. Return answer.

// Dry Run:
//
// Input:
//
// n = 2
//
// Start:
//
// current = ""
//
// -----------------------
//
// Add "("
//
// current = "("
//
// -----------------------
//
// Add "("
//
// current = "(("
//
// -----------------------
//
// Add ")"
//
// current = "(()"
//
// -----------------------
//
// Add ")"
//
// current = "(())"
//
// Store:
//
// ["(())"]
//
// -----------------------
//
// Backtrack
//
// current = "()"
//
// -----------------------
//
// Add "("
//
// current = "()("
//
// -----------------------
//
// Add ")"
//
// current = "()()"
//
// Store:
//
// ["(())","()()"]
//
// -----------------------
//
// Final Answer:
//
// ["(())","()()"]

class Solution {

    public List<String> generateParenthesis(int n) {

        List<String> answer = new ArrayList<>();

        backtrack(answer, "", 0, 0, n);

        return answer;
    }

    public void backtrack(List<String> answer, String current,
                          int open, int close, int n) {

        if (current.length() == 2 * n) {
            answer.add(current);
            return;
        }

        if (open < n) {
            backtrack(answer, current + "(", open + 1, close, n);
        }

        if (close < open) {
            backtrack(answer, current + ")", open, close + 1, n);
        }
    }
}

// Interview Explanation:
//
// 1. I used Backtracking to
//    generate all valid
//    parentheses combinations.
//
// 2. I maintained two counters:
//
//      open
//      close
//
// 3. I added '(' only if
//    open < n.
//
// 4. I added ')' only if
//    close < open.
//
// 5. Whenever the string
//    length became 2*n,
//    I stored it in the
//    answer list.
//
// 6. Finally, I returned
//    all valid combinations.
//
// Time Complexity: O(4^n / √n)
//
// Space Complexity: O(n)

