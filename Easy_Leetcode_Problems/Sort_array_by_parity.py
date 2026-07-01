
# 🚀 LeetCode 977 - Squares of a Sorted Array

# 📝 Problem
# Given a sorted integer array `nums`.
# Return an array containing the square of each number.
# The returned array must also be sorted in non-decreasing order.

# 💡 Logic
# Use two pointers: left and right.
# Compare the absolute values of the leftmost and rightmost elements.
# The larger absolute value gives the larger square.
# Place the larger square at the last available position in the answer array.
# Move the corresponding pointer.
# Repeat until all elements are processed.

# 📌 Algorithm
# 1. Create an answer array of the same size as nums.
# 2. Initialize left = 0.
# 3. Initialize right = len(nums) - 1.
# 4. Initialize pos = len(nums) - 1.
# 5. Compare abs(nums[left]) and abs(nums[right]).
# 6. Store the larger square at ans[pos].
# 7. Move the corresponding pointer.
# 8. Decrease pos by 1.
# 9. Repeat until left > right.
# 10. Return the answer array.

# 💻 Python Code


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
```

# ⏱️ Time Complexity
# O(n)

# 📦 Space Complexity
# O(n)

# 🎯 Interview Explanation
# I used the Two Pointer approach.
# One pointer starts from the beginning and another from the end.
# I compare the absolute values of both elements.
# The larger absolute value produces the larger square.
# I place that square at the end of the result array.
# Then I move the corresponding pointer.
# This continues until all elements are processed.
# The solution works in O(n) time and O(n) extra space.

