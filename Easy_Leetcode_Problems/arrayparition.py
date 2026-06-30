
# Algorithm:
#
# 1. Sort the array in ascending order.
#
# 2. Initialize a variable total = 0.
#
# 3. Traverse the sorted array with a step of 2.
#
# 4. Add every first element of each pair to total.
#
# 5. Return total as the maximum possible sum.

# Logic:
#
# 1. Sort the array so that smaller numbers come before larger numbers.
#
# 2. Pair adjacent elements after sorting.
#
# 3. The first element of each pair is the minimum.
#
# 4. Adding all first elements gives the maximum possible sum.
#
# 5. Return the final sum.

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]

        return total
    
# Interview Explanation:
#
# 1. First, sort the array in ascending order.
#
# 2. Pair every two adjacent elements.
#
# 3. The first element in each pair is the minimum value.
#
# 4. Add all these minimum values to get the maximum possible sum.
#
# 5. Return the final answer.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)