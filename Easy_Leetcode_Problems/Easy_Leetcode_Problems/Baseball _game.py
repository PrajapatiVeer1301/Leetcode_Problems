# Logic:
#
# 1. Use a stack (list) to store all valid scores.
#
# 2. If the operation is a number,
#    add it to the stack.
#
# 3. If the operation is "C",
#    remove the last score.
#
# 4. If the operation is "D",
#    add double of the last score.
#
# 5. If the operation is "+",
#    add the sum of the last two scores.
#
# 6. Return the sum of all scores in the stack.

# Algorithm:
#
# 1. Create an empty stack.
#
# 2. Traverse each operation.
#
# 3. If it is an integer,
#    push it into the stack.
#
# 4. If it is "C",
#    pop the last score.
#
# 5. If it is "D",
#    push 2 × last score.
#
# 6. If it is "+",
#    push the sum of the last two scores.
#
# 7. Return the sum of all elements in the stack.

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for op in operations:

            if op == "C":
                stack.pop()

            elif op == "D":
                stack.append(2 * stack[-1])

            elif op == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(op))

        return sum(stack)
    


# Interview Explanation:
#
# 1. I used a stack to store all valid scores.
#
# 2. If the operation is a number,
#    I push it into the stack.
#
# 3. If the operation is "C",
#    I remove the last score.
#
# 4. If the operation is "D",
#    I add double of the previous score.
#
# 5. If the operation is "+",
#    I add the sum of the last two scores.
#
# 6. Finally, I return the sum of all scores in the stack.
#
# Time Complexity: O(n)
# Space Complexity: O(n)