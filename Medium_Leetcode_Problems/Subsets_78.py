# Logic:
#
# We use Backtracking to generate all possible subsets.
#
# For every element, there are 2 choices:
#
# 1. Take the element
# 2. Do not take the element
#
# Example:
#
# nums = [1,2]
#
# Decision Tree:
#
#             []
#           /    \
#       take 1   skip 1
#          /        \
#        [1]         []
#       /   \       /   \
#   take 2 skip 2 take 2 skip 2
#    [1,2]  [1]    [2]   []
#
# Final subsets:
#
# [[], [1], [2], [1,2]]
#
# So, we try every possible choice
# and generate all subsets.
#
# Main idea:
#
# Choose → Explore → Backtrack
#
# Choose:
# Add the element to the current subset.
#
# Explore:
# Recursively process the remaining elements.
#
# Backtrack:
# Remove the last element and try
# another possibility.
#
# Time Complexity: O(n * 2^n)
#
# Space Complexity: O(n)
# (excluding the output)

# Algorithm:
#
# 1. Create an empty result list.
#
# 2. Create an empty current subset.
#
# 3. Start backtracking from index 0.
#
# 4. Add the current subset to result.
#
# 5. For every element:
#
#       Add the element to current.
#
#       Recursively generate
#       remaining subsets.
#
#       Remove the element
#       (backtracking).
#
# 6. Return result.

# Dry Run:
#
# Start:
#
# current = []
# result = [[]]
#
# -------------------------
#
# Choose 1
#
# current = [1]
# result = [[], [1]]
#
# Choose 2
#
# current = [1,2]
# result = [[], [1], [1,2]]
#
# Choose 3
#
# current = [1,2,3]
# result = [[], [1], [1,2], [1,2,3]]
#
# Backtrack
#
# Remove 3
# current = [1,2]
#
# Remove 2
# current = [1]
#
# Choose 3
#
# current = [1,3]
# result includes [1,3]
#
# Backtrack
#
# Remove 3
# current = [1]
#
# Remove 1
# current = []
#
# Choose 2
#
# current = [2]
#
# Choose 3
#
# current = [2,3]
#
# result includes [2,3]
#
# Backtrack
#
# Remove 3
# Remove 2
#
# Choose 3
#
# current = [3]
#
# result includes [3]
#
# Final Result:
#
# [[], [1], [1,2], [1,2,3],
#  [1,3], [2], [2,3], [3]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        current = []

        def backtrack(index):

            # Add current subset
            result.append(current.copy())

            # Try every remaining element
            for i in range(index, len(nums)):

                # Choose
                current.append(nums[i])

                # Explore
                backtrack(i + 1)

                # Backtrack
                current.pop()

        backtrack(0)

        return result

# Interview Explanation:
#
# I used Backtracking to generate
# all possible subsets.
#
# For every element, I decide whether
# to include it in the current subset.
#
# I add the current subset to the result
# because every state represents a
# valid subset.
#
# Then I recursively process the
# remaining elements.
#
# After recursion, I remove the last
# element using backtracking and try
# the next possibility.
#
# Since every element has two choices,
# include or exclude, there are
# 2^n possible subsets.
#
# Time Complexity: O(n * 2^n)
#
# Space Complexity: O(n)
# excluding the output.

##  ⭐ Main lines to remember

current.append(nums[i])
backtrack(i + 1)
current.pop()
    