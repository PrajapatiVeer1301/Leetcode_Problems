# 1. Find every operator in the expression.
#
# 2. When an operator is found, split the expression
#    into two parts:
#
#       Left  = part before the operator
#       Right = part after the operator
#
# 3. Recursively find all possible results for the Left part.
#
# 4. Recursively find all possible results for the Right part.
#
# 5. Apply the current operator to every combination
#    of Left and Right results.
#
# 6. Add all calculated results to the answer list.
#
# 7. If there is no operator in the expression,
#    it is a single number, so convert it to an integer
#    and return it.

#------- Algorithm-------
# Step 1:
# Create a recursive function solve(expression).
#
# Step 2:
# Create an empty result list.
#
# Step 3:
# Traverse every character in expression.
#
# Step 4:
# If character is '+', '-' or '*':
#
#       Split expression into left and right.
#
# Step 5:
# Recursively calculate:
#
#       leftResults
#       rightResults
#
# Step 6:
# Combine every left result with every right result.
#
# Step 7:
# Add the calculated values to result.
#
# Step 8:
# If no operator was found, return the number itself.
#
# Step 9:
# Return all possible results.

# ----------- Dry Run -----------
# Input:
# expression = "2-1-1"
#
# First '-':
#
# Left  = "2"
# Right = "1-1"
#
# solve("2") → [2]
#
# solve("1-1"):
#
# Left  = "1"
# Right = "1"
#
# 1 - 1 = 0
#
# Therefore:
#
# 2 - 0 = 2
#
# Result = [2]
#
#
# --------------------------------
#
# Second '-' in "2-1-1":
#
# Left  = "2-1"
# Right = "1"
#
# solve("2-1"):
#
# 2 - 1 = 1
#
# solve("1") → [1]
#
# Therefore:
#
# 1 - 1 = 0
#
# Result = [2, 0]
#
# Final Output:
#
# [2, 0]
#
# Order does not matter,
# so [0, 2] is also correct.


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def solve(exp):

            result = []

            for i in range(len(exp)):

                if exp[i] in "+-*":

                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for a in left:
                        for b in right:

                            if exp[i] == '+':
                                result.append(a + b)

                            elif exp[i] == '-':
                                result.append(a - b)

                            else:
                                result.append(a * b)

            # If there is no operator,
            # the expression is just a number.
            if not result:
                result.append(int(exp))

            return result

        return solve(expression)

#--------- 🎯 Interview Explanation -----------
# I used recursion and divide-and-conquer.
#
# I considered every operator as a possible place
# to split the expression into two parts.
#
# For each operator, I recursively calculated all
# possible results of the left and right parts.
#
# Then I combined every left result with every
# right result using the current operator.
#
# If the expression contains no operator, it is
# simply a number, so I return that number.
#
# This generates every possible way of adding
# parentheses to the expression.
#
# Time Complexity:
# Exponential, because the number of possible
# parenthesizations can grow exponentially.
#
# Space Complexity:
# O(n) recursion depth, excluding the output list.

#--------- ⭐ Remember this pattern ----------

Expression
     |
  Operator
     |
 ┌───┴───┐
Left   Right
 |       |
Recursion
 |       |
Results Results
 └───┬───┘
   Combine
     |
 All Results