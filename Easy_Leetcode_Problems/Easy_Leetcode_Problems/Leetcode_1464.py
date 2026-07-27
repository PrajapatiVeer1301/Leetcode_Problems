# Logic:
#
# 1. Find the largest number.
#
# 2. Find the second largest number.
#
# 3. Subtract 1 from both.
#
# 4. Multiply them.
#
# 5. Return the result.

# Algorithm:
#
# 1. Initialize first = 0, second = 0.
#
# 2. Traverse the array.
#
# 3. Update first and second largest numbers.
#
# 4. Return:
#
#      (first - 1) * (second - 1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        first = 0
        second = 0

        for num in nums:

            if num >= first:
                second = first
                first = num

            elif num > second:
                second = num

        return (first - 1) * (second - 1)

# Interview Explanation:
#
# 1. I traversed the array only once.
#
# 2. I kept track of the largest and
#    second largest elements.
#
# 3. After finding them,
#    I applied the formula:
#
#       (first - 1) * (second - 1)
#
# 4. This avoids sorting the array
#    and provides an efficient solution.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)