# ⭐ MAIN LOGIC
#
# We use a Stack to check whether the brackets are valid.
#
# - When we find an opening bracket, we push it into the stack.
# - When we find a closing bracket, we check it with the
#   top element of the stack.
# - If they do not match, return False.
# - After processing the complete string, if the stack is empty,
#   return True.
#
#
# Example:
#
# s = "([])"
#
# Processing:
#
# ( → push
# [ → push
# ] → matches [ → pop
# ) → matches ( → pop
#
# Stack is empty, so the answer is:
#
# True
#
#
# 🔄 ALGORITHM
#
# 1. Create an empty stack.
#
# 2. Traverse every character of the string.
#
# 3. If the character is an opening bracket:
#
#       '(' or '[' or '{'
#
#    Push it into the stack.
#
# 4. If the character is a closing bracket:
#
#       ')' or ']' or '}'
#
#    Check whether the stack is empty.
#
#    If the stack is empty:
#        Return False.
#
# 5. Check whether the top element of the stack
#    matches the current closing bracket.
#
#    If it does not match:
#        Return False.
#
# 6. If it matches:
#       Pop the opening bracket from the stack.
#
# 7. After processing all characters:
#
#       If stack is empty:
#           Return True
#
#       Otherwise:
#           Return False
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def isValid(self, s: str) -> bool:

        # Stack to store opening brackets
        stack = []

        # Store the matching opening bracket
        # for every closing bracket
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Traverse every character
        for ch in s:

            # If it is an opening bracket
            if ch in '([{':
                
                # Push the opening bracket into the stack
                stack.append(ch)

            # If it is a closing bracket
            else:

                # If stack is empty, there is no
                # corresponding opening bracket
                if not stack:
                    return False

                # Check whether the top opening bracket
                # matches the current closing bracket
                if stack[-1] != pairs[ch]:
                    return False

                # Remove the matched opening bracket
                stack.pop()

        # The string is valid only if
        # no opening brackets are left
        return len(stack) == 0


# 🧪 DRY RUN
#
# Example:
#
# s = "([)]"
#
#
# Step 1:
#
# Character = '('
#
# Opening bracket → push
#
# stack = ['(']
#
#
# Step 2:
#
# Character = '['
#
# Opening bracket → push
#
# stack = ['(', '[']
#
#
# Step 3:
#
# Character = ')'
#
# Expected opening bracket:
#
# '('
#
# But stack top is:
#
# '['
#
# '[' != '('
#
# Therefore:
#
# return False
#
#
# Final Answer:
#
# False
#
#
# 🧪 ANOTHER EXAMPLE
#
# s = "()[]{}"
#
# Processing:
#
# ( → push
# ) → matches ( → pop
#
# [ → push
# ] → matches [ → pop
#
# { → push
# } → matches { → pop
#
#
# Final stack:
#
# []
#
# Therefore:
#
# True
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I use a stack to validate the brackets.
# Whenever I encounter an opening bracket, I push it
# onto the stack.
#
# For a closing bracket, I first check whether the stack
# is empty and then compare it with the top opening bracket.
# If they do not match, I return false.
#
# If they match, I remove the opening bracket from the stack.
#
# After processing the entire string, the string is valid
# only when the stack is empty."
#
#
# ⏱️ COMPLEXITY
#
# Time Complexity: O(n)
#
# Each character is processed exactly once.
#
# Space Complexity: O(n)
#
# In the worst case, all characters can be opening brackets,
# so the stack can contain n elements.