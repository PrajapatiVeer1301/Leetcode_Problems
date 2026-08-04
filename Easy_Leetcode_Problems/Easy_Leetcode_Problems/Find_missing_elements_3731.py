# Logic:
#
# 1. Find the smallest number.
#
# 2. Find the largest number.
#
# 3. Store all array elements
#    in a set.
#
# 4. Traverse every number from
#    smallest to largest.
#
# 5. If a number is not found
#    in the set, it is missing.
#
# 6. Add it to the answer list.
#
# 7. Return the answer.

# Algorithm:
#
# 1. Find min(nums) and max(nums).
#
# 2. Convert nums into a set.
#
# 3. Create an empty list.
#
# 4. Traverse from min to max.
#
# 5. If the current number
#    is not in the set,
#    add it to the answer.
#
# 6. Return the answer list.

# Dry Run:
#
# Input:
#
# nums = [1,4,2,5]
#
# start = 1
# end = 5
#
# set = {1,2,4,5}
#
# answer = []
#
# -----------------------
#
# i = 1
#
# Present
#
# answer = []
#
# -----------------------
#
# i = 2
#
# Present
#
# answer = []
#
# -----------------------
#
# i = 3
#
# Missing
#
# answer = [3]
#
# -----------------------
#
# i = 4
#
# Present
#
# answer = [3]
#
# -----------------------
#
# i = 5
#
# Present
#
# answer = [3]
#
# -----------------------
#
# Return:
#
# [3]

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        start = min(nums)
        end = max(nums)

        numSet = set(nums)

        answer = []

        for i in range(start, end + 1):

            if i not in numSet:
                answer.append(i)

        return answer

# Interview Explanation:
#
# 1. I first found the smallest
#    and largest numbers.
#
# 2. I converted the array into
#    a set for O(1) lookup.
#
# 3. Then I traversed every number
#    in the complete range.
#
# 4. If a number was not found
#    in the set, I added it
#    to the answer.
#
# 5. Finally, I returned the
#    sorted list of missing numbers.
#
# Time Complexity: O(n + range)
#
# Space Complexity: O(n)













