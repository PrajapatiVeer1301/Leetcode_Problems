# Logic:
#
# 1. Find the minimum element.
#
# 2. Find the maximum element.
#
# 3. Find the GCD using the Euclidean Algorithm.
#
# 4. Return the GCD.

# Algorithm:
#
# 1. Find min(nums).
#
# 2. Find max(nums).
#
# 3. While max is not 0:
#      remainder = min % max
#      min = max
#      max = remainder
#
# 4. Return min.

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        small = min(nums)
        large = max(nums)

        while large != 0:
            small, large = large, small % large

        return small
    
# Interview Explanation:
#
# 1. First, I found the smallest and largest elements.
#
# 2. Then I used the Euclidean Algorithm
#    to compute their GCD.
#
# 3. The algorithm repeatedly replaces
#    the larger number with the remainder
#    until the remainder becomes zero.
#
# 4. The remaining number is the GCD.
#
# Time Complexity: O(n + log(max))
# Space Complexity: O(1)

















