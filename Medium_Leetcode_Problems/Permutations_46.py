# Logic:
#
# We use Backtracking to generate
# all possible permutations.
#
# For every position, we can choose
# any element that has not been used.
#
# Example:
#
# nums = [1,2,3]
#
# Start:
# []
#
# Choose 1:
# [1]
#
# Then choose 2:
# [1,2]
#
# Then choose 3:
# [1,2,3]
#
# Backtrack and try another choice:
# [1,3,2]
#
# Then start with 2:
# [2,1,3]
# [2,3,1]
#
# Then start with 3:
# [3,1,2]
# [3,2,1]
#
# Main idea:
#
# Choose → Explore → Backtrack
#
# We use a "used" array to keep track
# of elements already included.

# Algorithm:
#
# 1. Create an empty result list.
#
# 2. Create an empty current list.
#
# 3. Create a used array of False values.
#
# 4. Start backtracking.
#
# 5. If current length == nums length:
#       Add a copy of current to result.
#
# 6. Otherwise, loop through all elements:
#
#       If element is already used:
#           skip it.
#
#       Mark element as used.
#
#       Add element to current.
#
#       Recursively generate permutations.
#
#       Remove element from current.
#
#       Mark element as unused.
#
# 7. Return result.

# Dry Run:
#
# nums = [1,2,3]
#
# Start:
#
# current = []
# used = [F,F,F]
#
# -------------------------
#
# Choose 1:
#
# current = [1]
# used = [T,F,F]
#
# Choose 2:
#
# current = [1,2]
# used = [T,T,F]
#
# Choose 3:
#
# current = [1,2,3]
# used = [T,T,T]
#
# Length == 3
#
# Add [1,2,3]
#
# -------------------------
#
# Backtrack:
#
# Remove 3
# current = [1,2]
#
# Remove 2
# current = [1]
#
# Choose 3:
#
# current = [1,3]
#
# Choose 2:
#
# current = [1,3,2]
#
# Add [1,3,2]
#
# -------------------------
#
# Backtrack completely:
#
# current = []
#
# Choose 2:
#
# [2,1,3]
# [2,3,1]
#
# Choose 3:
#
# [3,1,2]
# [3,2,1]
#
# -------------------------
#
# Final Result:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():

            # If permutation is complete
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):

                # Skip already used element
                if used[i]:
                    continue

                # Choose
                used[i] = True
                current.append(nums[i])

                # Explore
                backtrack()

                # Backtrack
                current.pop()
                used[i] = False

        backtrack()

        return result

# Interview Explanation:
#
# I used Backtracking to generate
# all possible permutations.
#
# At each position, I try every element
# that has not been used yet.
#
# I maintain a "used" array to make sure
# the same element is not selected twice
# in the same permutation.
#
# When the current permutation reaches
# the size of nums, I add it to the result.
#
# After the recursive call, I remove the
# selected element and mark it unused.
# This is the backtracking step.
#
# Since there are n! permutations and
# each permutation takes O(n) time to copy,
#
# Time Complexity: O(n × n!)
#
# Space Complexity: O(n)
# excluding the output.

##  ⭐ Important Lines
used[i] = True
current.append(nums[i])

backtrack()

current.pop()
used[i] = False

