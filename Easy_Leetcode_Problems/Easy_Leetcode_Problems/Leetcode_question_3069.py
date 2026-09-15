# 💡 Logic
#
# We will maintain two arrays:
#
# arr1
# arr2
#
# First, put the first element of nums into arr1.
#
# Then, put the second element of nums into arr2.
#
# After that, start from the third element, nums[2].
#
# For every remaining element:
#
# If the last element of arr1 is greater than
# the last element of arr2:
#
#     arr1.append(nums[i])
#
# Otherwise:
#
#     arr2.append(nums[i])
#
# Finally, concatenate arr1 and arr2:
#
#     return arr1 + arr2


# 🔄 Algorithm
#
# 1. Add nums[0] to arr1.
#
# 2. Add nums[1] to arr2.
#
# 3. Start a loop from index 2 to the end of nums.
#
# 4. Compare the last elements of arr1 and arr2.
#
# 5. If arr1's last element is greater than arr2's last element:
#       Add nums[i] to arr1.
#
# 6. Otherwise:
#       Add nums[i] to arr2.
#
# 7. After processing all elements, concatenate arr1 and arr2.
#
# 8. Return the final result.


# 🧪 Dry Run
#
# Example 1:
#
# nums = [2, 1, 3]
#
# Initially:
#
# arr1 = [2]
# arr2 = [1]
#
# Now process 3:
#
# arr1[-1] = 2
# arr2[-1] = 1
#
# Check:
#
# 2 > 1 → True
#
# Therefore, add 3 to arr1:
#
# arr1 = [2, 3]
# arr2 = [1]
#
# Finally:
#
# arr1 + arr2
# = [2, 3] + [1]
# = [2, 3, 1]
#
# Answer = [2, 3, 1]


# 🧪 Dry Run - Example 2
#
# nums = [5, 4, 3, 8]
#
# Initially:
#
# arr1 = [5]
# arr2 = [4]
#
#
# Process 3:
#
# arr1[-1] = 5
# arr2[-1] = 4
#
# 5 > 4 → True
#
# Add 3 to arr1:
#
# arr1 = [5, 3]
# arr2 = [4]
#
#
# Process 8:
#
# arr1[-1] = 3
# arr2[-1] = 4
#
# 3 > 4 → False
#
# Add 8 to arr2:
#
# arr1 = [5, 3]
# arr2 = [4, 8]
#
#
# Finally:
#
# [5, 3] + [4, 8]
# = [5, 3, 4, 8]
#
# Answer = [5, 3, 4, 8]


# 🎯 Interview Explanation
#
# "I will maintain two arrays, arr1 and arr2.
#
# I put the first element into arr1 and the second element
# into arr2.
#
# Then I iterate from the third element to the end.
#
# For each element, I compare the last elements of arr1 and arr2.
#
# If the last element of arr1 is greater, I append the current
# element to arr1.
#
# Otherwise, I append it to arr2.
#
# Finally, I concatenate arr1 and arr2 and return the result."


# ⭐ Key Trick
#
# The most important trick is:
#
# arr1[-1]
#
# It gives the last element of arr1.
#
# Similarly:
#
# arr2[-1]
#
# It gives the last element of arr2.
#
# Therefore, we can easily compare them:
#
# if arr1[-1] > arr2[-1]:
#
# Also, Python allows us to concatenate two arrays using:
#
# arr1 + arr2
#
# This gives the final result.


# ⏱️ Complexity
#
# Time Complexity: O(n)
#
# We process every element exactly once.
#
#
# Space Complexity: O(n)
#
# arr1 and arr2 together contain all n elements.


# 🧑‍💻 Python Code

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        # Put the first element into arr1
        arr1 = [nums[0]]

        # Put the second element into arr2
        arr2 = [nums[1]]

        # Process all remaining elements
        for i in range(2, len(nums)):

            # Compare the last elements of both arrays
            if arr1[-1] > arr2[-1]:

                # Add the current element to arr1
                arr1.append(nums[i])

            else:

                # Add the current element to arr2
                arr2.append(nums[i])

        # Concatenate arr1 and arr2
        return arr1 + arr2