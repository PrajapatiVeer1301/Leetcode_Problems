
# Algorithm:
#
# 1. Create an answer array of the same size.
#
# 2. Initialize two pointers:
#    - left = 0
#    - right = last index
#
# 3. Compare the absolute values of nums[left] and nums[right].
#
# 4. Place the larger square at the end of the answer array.
#
# 5. Move the corresponding pointer.
#
# 6. Repeat until left > right.
#
# 7. Return the answer array.

# Logic:
#
# 1. The largest square is always at either end of the sorted array.
#
# 2. Compare the absolute values of the leftmost and rightmost elements.
#
# 3. Square the larger value and place it at the current last position.
#
# 4. Move the corresponding pointer.
#
# 5. Continue until all elements are processed.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[pos] = nums[left] * nums[left]
                left += 1
            else:
                ans[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return ans
    
    # Interview Explanation:
#
# 1. Since the array is already sorted, the largest square will be
#    either at the beginning or the end.
#
# 2. Use two pointers: one at the start and one at the end.
#
# 3. Compare their absolute values.
#
# 4. Place the larger square at the end of the result array.
#
# 5. Move the corresponding pointer and repeat.
#
# 6. Return the sorted squared array.
#
# Time Complexity: O(n)
# Space Complexity: O(n)