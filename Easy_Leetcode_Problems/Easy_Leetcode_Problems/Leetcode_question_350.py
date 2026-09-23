# 💡 Logic
#
# We will use a frequency count to find the intersection.
#
# - Store the frequency of every element in nums1 in a dictionary.
# - Then check every element of nums2.
# - If the element is available in nums1, add it to the result.
# - Decrease its frequency by 1.
# - When its frequency becomes 0, we cannot add that element again.
#
#
# ⭐ Key Trick
#
# count[num] -= 1
#
# This decreases the available frequency of the element.
#
# It ensures that duplicate elements appear in the result
# only as many times as they appear in both arrays.
#
#
# 🔄 Algorithm
#
# 1. Count the frequency of every element in nums1.
#
# 2. Traverse through nums2.
#
# 3. If num exists in the dictionary and its frequency is greater than 0:
#    - Add num to the result.
#    - Decrease its frequency by 1.
#
# 4. Return the result.
#
#
# 🧑‍💻 Python Code
#
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # Store the frequency of elements in nums1
        count = {}

        # Count each element
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # Store the intersection result
        result = []

        # Check every element in nums2
        for num in nums2:

            # Check if the element is available
            if num in count and count[num] > 0:

                # Add the element to the result
                result.append(num)

                # Decrease its available frequency
                count[num] -= 1

        return result
#
#
# 🧪 Dry Run
#
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
#
#
# Frequency of nums1:
#
# 1 → 2
# 2 → 2
#
#
# Process nums2:
#
# First 2:
#
# 2 is available
# result = [2]
# frequency of 2 = 1
#
#
# Second 2:
#
# 2 is available
# result = [2, 2]
# frequency of 2 = 0
#
#
# Final result:
#
# [2, 2]
#
#
# 🎯 Interview Explanation
#
# "I use a hash map to store the frequency of every element
# in the first array. Then I traverse the second array.
# If the current element exists in the hash map and its
# remaining frequency is greater than zero, I add it to the
# result and decrease its frequency.
#
# This ensures that every element appears in the result
# only as many times as it appears in both arrays."
#
#
# ⏱️ Complexity
#
# Time Complexity: O(n + m)
#
# We traverse nums1 once and nums2 once.
#
# Space Complexity: O(n)
#
# The hash map stores frequencies of elements from nums1.
#
# n = length of nums1
# m = length of nums2
#
#
# 🔹 Follow-up
#
# 1. If both arrays are already sorted:
#
#    Use two pointers.
#    Compare the elements of both arrays and move the
#    appropriate pointer.
#    This can use O(1) extra space, excluding the result.
#
#
# 2. If nums1 is much smaller than nums2:
#
#    Build the frequency map using the smaller array
#    and scan the larger array.
#    This reduces the extra space required.
#
#
# 3. If nums2 is stored on disk and memory is limited:
#
#    Store the frequency information for the array that
#    fits in memory.
#    Then process nums2 in chunks instead of loading the
#    entire array into memory at once.