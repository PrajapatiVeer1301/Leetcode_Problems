# 💡 LOGIC
#
# We need to split the parentheses string into two groups:
#
# Group 0 → A
# Group 1 → B
#
# Both groups must remain valid parentheses strings.
#
# The main goal is to minimize:
#
#     max(depth(A), depth(B))
#
#
# ⭐ KEY TRICK
#
# We track the current nesting depth.
#
# For every opening parenthesis '(':
#
#     depth += 1
#
# For every closing parenthesis ')':
#
#     use the current depth
#     depth -= 1
#
#
# We assign the group using:
#
#     depth % 2
#
# This alternates the nested parentheses between group 0
# and group 1.
#
# Therefore, deeply nested parentheses are distributed
# between the two groups.
#
#
# 🔄 ALGORITHM
#
# 1. Initialize:
#
#       depth = 0
#
# 2. Traverse every character in seq.
#
# 3. If the character is '(':
#
#       Increase depth by 1.
#       Assign:
#           depth % 2
#
# 4. If the character is ')':
#
#       Assign:
#           depth % 2
#
#       Then decrease depth by 1.
#
# 5. Return the answer array.
#
#
# ⭐ IMPORTANT
#
# For '(' we increase the depth BEFORE assigning the group.
#
# For ')' we assign the group BEFORE decreasing the depth.
#
# This keeps the opening and closing parentheses of the
# same pair in the same group.
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:

        # Store the current nesting depth
        depth = 0

        # Store the group assignment
        answer = []

        # Traverse every character in the sequence
        for ch in seq:

            # If it is an opening parenthesis
            if ch == '(':

                # Increase the current depth
                depth += 1

                # Assign the parenthesis to group 0 or 1
                answer.append(depth % 2)

            # If it is a closing parenthesis
            else:

                # Assign the parenthesis using current depth
                answer.append(depth % 2)

                # Decrease the current depth
                depth -= 1

        # Return the group assignment
        return answer


# 🧪 DRY RUN
#
# Example:
#
# seq = "(()())"
#
# Initially:
#
# depth = 0
#
#
# Character 1: '('
#
# depth = 1
# group = 1 % 2 = 1
#
# answer = [1]
#
#
# Character 2: '('
#
# depth = 2
# group = 2 % 2 = 0
#
# answer = [1, 0]
#
#
# Character 3: ')'
#
# group = 2 % 2 = 0
# depth = 1
#
# answer = [1, 0, 0]
#
#
# Character 4: '('
#
# depth = 2
# group = 2 % 2 = 0
#
# answer = [1, 0, 0, 0]
#
#
# Character 5: ')'
#
# group = 2 % 2 = 0
# depth = 1
#
# answer = [1, 0, 0, 0, 0]
#
#
# Character 6: ')'
#
# group = 1 % 2 = 1
# depth = 0
#
# answer = [1, 0, 0, 0, 0, 1]
#
#
# Final Answer:
#
# [1, 0, 0, 0, 0, 1]
#
# The problem allows any optimal valid assignment,
# so the answer does not need to exactly match the example.
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I track the current nesting depth while traversing
# the parentheses string. For an opening parenthesis, I
# first increase the depth and assign the parenthesis
# according to the parity of the depth.
#
# For a closing parenthesis, I assign it using the current
# depth and then decrease the depth.
#
# Using depth % 2 alternates nested parentheses between
# the two groups. This distributes the nesting depth as
# evenly as possible and minimizes the maximum depth."
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
# The answer array contains n elements.
#
# Extra Working Space: O(1)
#
# Only depth and a few variables are used apart from
# the required answer array.