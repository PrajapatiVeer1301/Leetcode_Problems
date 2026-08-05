# Logic:
#
# 1. Use Backtracking.
#
# 2. Keep track of:
#      Current String
#      Open Brackets
#      Close Brackets
#
# 3. Add '(' if openCount < n.
#
# 4. Add ')' only if
#    closeCount < openCount.
#
# 5. When the string length
#    becomes 2*n,
#    store it.
#
# 6. Return all combinations.

# Algorithm:
#
# 1. Create an empty answer list.
#
# 2. Start recursion with:
#
#      current = ""
#      open = 0
#      close = 0
#
# 3. If open < n,
#    add '('.
#
# 4. If close < open,
#    add ')'.
#
# 5. If current length = 2*n,
#    store it.
#
# 6. Return answer.

# Dry Run:
#
# Input:
#
# n = 2
#
# Start:
#
# ""
#
# ----------------------
#
# Add "("
#
# "("
#
# ----------------------
#
# Add "("
#
# "(("
#
# ----------------------
#
# Add ")"
#
# "(()"
#
# ----------------------
#
# Add ")"
#
# "(())"
#
# Store
#
# ----------------------
#
# Backtrack
#
# "()"
#
# ----------------------
#
# Add "("
#
# "()("
#
# ----------------------
#
# Add ")"
#
# "()()"
#
# Store
#
# ----------------------
#
# Final Answer:
#
# ["(())","()()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []

        def backtrack(current, openCount, closeCount):

            if len(current) == 2 * n:
                answer.append(current)
                return

            if openCount < n:
                backtrack(current + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(current + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)

        return answer

# Interview Explanation:
#
# 1. I used Backtracking to
#    generate all valid
#    parentheses combinations.
#
# 2. I maintained two counters:
#      openCount
#      closeCount
#
# 3. I added '(' only if
#    openCount < n.
#
# 4. I added ')' only if
#    closeCount < openCount.
#
# 5. Whenever the string
#    length became 2*n,
#    I stored the result.
#
# Time Complexity: O(4^n / √n)
#
# Space Complexity: O(n)