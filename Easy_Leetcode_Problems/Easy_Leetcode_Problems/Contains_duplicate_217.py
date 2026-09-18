# 💡 Logic
#
# We will use a Set to find duplicate elements.
#
# A Set does not store duplicate values.
#
# For example:
#
# nums = [1, 2, 3, 1]
#
# set(nums) = {1, 2, 3}
#
# len(nums) = 4
# len(set(nums)) = 3
#
# Since both lengths are different, a duplicate exists.
#
# Therefore:
#
# len(nums) != len(set(nums))
#
# If this condition is True, the array contains a duplicate.
#
#
# 🔄 Algorithm
#
# 1. Convert nums into a Set.
#
# 2. Compare the length of nums with the length of the Set.
#
# 3. If both lengths are different:
#    → Return True because a duplicate exists.
#
# 4. If both lengths are the same:
#    → Return False because all elements are distinct.
#
#
# 🧑‍💻 Python Code
#
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#
#         # Convert the array into a set
#         unique = set(nums)
#
#         # If lengths are different, duplicates exist
#         if len(nums) != len(unique):
#             return True
#
#         # All elements are distinct
#         return False
#
#
# ⭐ Shortest Code
#
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return len(nums) != len(set(nums))
#
#
# 🧪 Example
#
# nums = [1, 2, 3, 1]
#
# Original array:
# [1, 2, 3, 1]
#
# Set:
# {1, 2, 3}
#
# Length of nums = 4
# Length of set = 3
#
# 4 != 3 → True
#
# Therefore, a duplicate exists.
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)
#
# n = number of elements in the array.
#
#
# 🎯 Interview Explanation
#
# "I use a Set to detect duplicate elements.
# A Set stores only unique values, so if the length of the
# original array is different from the length of the Set,
# it means that at least one element appeared more than once.
# Therefore, I return True when the lengths are different;
# otherwise, I return False."