# 💡 Logic
#
# We use a variable called `depth` to track the current
# nesting level of parentheses.
#
# - When '(' is found, increase depth by 1.
# - When ')' is found, decrease depth by 1.
# - After every opening parenthesis, compare depth with max_depth.
# - The largest value of depth is the answer.
#
#
# 🔄 Algorithm
#
# 1. Initialize depth = 0.
#
# 2. Initialize max_depth = 0.
#
# 3. Traverse every character in the string.
#
# 4. If the character is '(':
#       Increase depth by 1.
#
# 5. Update max_depth.
#
# 6. If the character is ')':
#       Decrease depth by 1.
#
# 7. Return max_depth.
#
#
# 🧑‍💻 Python Code

class Solution:
    def maxDepth(self, s: str) -> int:

        # Store the current nesting depth
        depth = 0

        # Store the maximum nesting depth
        max_depth = 0

        # Traverse every character in the string
        for ch in s:

            # If an opening parenthesis is found
            if ch == '(':

                # Increase the current depth
                depth += 1

                # Update the maximum depth
                max_depth = max(max_depth, depth)

            # If a closing parenthesis is found
            elif ch == ')':

                # Decrease the current depth
                depth -= 1

        # Return the maximum nesting depth
        return max_depth


# 🧪 Dry Run
#
# Example:
#
# s = "(1)+((2))+(((3)))"
#
# Processing:
#
# ( → depth = 1 → max_depth = 1
# ) → depth = 0
#
# ( → depth = 1
# ( → depth = 2 → max_depth = 2
# ) → depth = 1
# ) → depth = 0
#
# ( → depth = 1
# ( → depth = 2
# ( → depth = 3 → max_depth = 3
# ) → depth = 2
# ) → depth = 1
# ) → depth = 0
#
# Final:
#
# max_depth = 3
#
# Answer = 3
#
#
# 🎯 Interview Explanation
#
# "I use a counter to track the current nesting depth.
# Whenever I encounter an opening parenthesis, I increase
# the depth and update the maximum depth.
#
# Whenever I encounter a closing parenthesis, I decrease
# the depth.
#
# The maximum value reached by the depth counter is the
# maximum nesting depth of the parentheses."
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n)
# We traverse the string only once.
#
# Space Complexity: O(1)
# We use only two variables: depth and max_depth.