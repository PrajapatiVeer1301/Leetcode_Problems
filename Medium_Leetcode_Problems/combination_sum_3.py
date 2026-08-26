# ---------- 💡 Logic ----------

# 1. Create a result list.
#
# 2. Create a current list.
#
# 3. Create a backtracking function.
#
# 4. If:
#
#       len(current) == k
#
#    and:
#
#       remaining == 0
#
#    then add the current combination to result.
#
# 5. Choose numbers from 1 to 9.
#
# 6. Add the number to current.
#
# 7. Make a recursive call with the remaining sum.
#
# 8. After returning from recursion,
#    remove the last number from current.
#
# 9. Try the next number.
#
# 10. Finally, return result.


# ---------- 🔄 Algorithm ----------

# Step 1: Create:
#
#         result = []
#         current = []
#
# Step 2: Create a backtracking function:
#
#         backtrack(start, remaining)
#
# Step 3: If current contains k numbers:
#
#         If remaining == 0:
#             Add a copy of current to result.
#
#         Return.
#
# Step 4: Run a loop from start to 9.
#
# Step 5: Choose the current number:
#
#         current.append(i)
#
# Step 6: Recursively call:
#
#         backtrack(i + 1, remaining - i)
#
# Step 7: Remove the last number:
#
#         current.pop()
#
# Step 8: Return result.


# ---------- 🧪 Dry Run ----------

# Input:
# k = 3
# n = 7
#
# --------------------------------
#
# Start:
#
# current = []
# remaining = 7
#
# --------------------------------
#
# Choose 1:
#
# current = [1]
# remaining = 6
#
# --------------------------------
#
# Choose 2:
#
# current = [1,2]
# remaining = 4
#
# --------------------------------
#
# Choose 3:
#
# current = [1,2,3]
# remaining = 1
#
# We already selected 3 numbers,
# but remaining != 0.
#
# So this combination is invalid.
#
# Backtrack:
#
# current = [1,2]
#
# --------------------------------
#
# Choose 4:
#
# current = [1,2,4]
# remaining = 0
#
# We selected 3 numbers
# and remaining = 0.
#
# Therefore:
#
# Add [1,2,4]
#
# result = [[1,2,4]]
#
# --------------------------------
#
# Try other combinations...
#
# None of them produce sum 7
# using exactly 3 numbers.
#
# --------------------------------
#
# Final Answer:
#
# [[1,2,4]]


# ---------- 🐍 Python Code ----------

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        current = []

        def backtrack(start, remaining):

            # If k numbers are selected
            if len(current) == k:

                # Check whether sum is exactly n
                if remaining == 0:
                    result.append(current.copy())

                return

            # Try numbers from start to 9
            for i in range(start, 10):

                # Choose
                current.append(i)

                # Explore
                backtrack(i + 1, remaining - i)

                # Backtrack
                current.pop()

        backtrack(1, n)

        return result


# ---------- 🎯 Interview Explanation ----------

# I use backtracking to generate all possible combinations.
#
# The numbers are restricted to 1 through 9,
# and each number can be used only once.
#
# I maintain a current list containing the selected numbers
# and a remaining value representing the sum still needed.
#
# When current contains exactly k numbers,
# I check whether remaining is 0.
#
# If it is 0, the combination is valid,
# so I add a copy of it to the result.
#
# I call backtrack(i + 1, ...)
# instead of backtrack(i, ...)
# so that the same number cannot be selected again.
#
# Time Complexity:
# O(C(9,k) * k)
#
# Space Complexity:
# O(k)
# excluding the output.


# ---------- ⭐ Key Trick ----------

# Use i + 1:
#
# backtrack(i + 1, remaining - i)
#
# This prevents reusing the same number.
#
# Example:
#
# [1,2,4] ✅
#
# [1,4,2] ❌
#
# because combinations do not depend on order.
#
# Also:
#
# Numbers are always selected from left to right:
#
# 1 → 2 → 3 → ... → 9