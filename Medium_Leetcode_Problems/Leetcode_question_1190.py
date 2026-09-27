# 💡 Logic
#
# This problem can be solved using a Stack.
#
# When:
#
# - '(' is found → Save the current string in the stack.
# - ')' is found → Reverse the current string and combine it
#                  with the previous string from the stack.
# - A letter is found → Add it to the current string.
#
# This automatically processes the innermost parentheses first.
#
#
# 🔄 Algorithm
#
# 1. Create an empty stack.
#
# 2. Set current = empty string.
#
# 3. Traverse every character of the string.
#
# 4. If the character is '(':
#       Push current string into the stack.
#       Reset current to an empty string.
#
# 5. If the character is ')':
#       Reverse current.
#       Pop the previous string from the stack.
#       Combine previous string + reversed current.
#
# 6. If the character is a normal letter:
#       Add the character to current.
#
# 7. Finally, return current.
#
#
# 🧑‍💻 Python Code

class Solution:
    def reverseParentheses(self, s: str) -> str:

        # Stack is used to store strings before '('
        stack = []

        # Store the current string
        current = ""

        # Traverse every character in the string
        for ch in s:

            # If an opening parenthesis is found
            if ch == '(':

                # Save the current string in the stack
                stack.append(current)

                # Start a new string inside the parentheses
                current = ""

            # If a closing parenthesis is found
            elif ch == ')':

                # Reverse the current substring
                current = current[::-1]

                # Get the previous string from the stack
                previous = stack.pop()

                # Combine the previous string with the reversed substring
                current = previous + current

            # If it is a normal character
            else:

                # Add the character to the current string
                current += ch

        # Return the final string without parentheses
        return current


# 🧪 Dry Run
#
# Example:
#
# s = "(abcd)"
#
# Initially:
#
# stack = []
# current = ""
#
# When '(' is found:
#
# stack = [""]
# current = ""
#
# Process the characters:
#
# a → current = "a"
# b → current = "ab"
# c → current = "abc"
# d → current = "abcd"
#
# When ')' is found:
#
# current = "abcd"
#
# Reverse current:
#
# "abcd" → "dcba"
#
# Pop the previous string:
#
# previous = ""
#
# Combine:
#
# current = "" + "dcba"
#        = "dcba"
#
# Final Answer:
#
# "dcba"
#
#
# 🧪 Example 2
#
# s = "(u(love)i)"
#
# First, process the inner parentheses:
#
# "love" → "evol"
#
# Then the outer string becomes:
#
# "uevoli"
#
# Reverse the outer substring:
#
# "uevoli" → "iloveu"
#
# Final Answer:
#
# "iloveu"
#
#
# 🎯 Interview Explanation
#
# "I use a stack to handle nested parentheses.
# When I encounter an opening parenthesis, I save the current
# string on the stack and start a new substring.
#
# When I encounter a closing parenthesis, I reverse the current
# substring and append it to the previous string stored in the stack.
#
# This naturally processes the innermost parentheses first.
# Finally, I return the current string, which contains no
# parentheses."
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n²)
#
# In the worst case, nested strings may be reversed and
# concatenated multiple times.
#
# Space Complexity: O(n)
#
# The stack and stored strings can require O(n) space.
#
# Since n <= 2000, this approach is suitable.