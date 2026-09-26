# 💡 LOGIC
#
# We are given an array nums of length n.
#
# Every number in nums is in the range [1, n].
#
# We need to find all numbers from 1 to n
# that do not appear in the array.
#
#
# ⭐ IMPORTANT TRICK
#
# We should solve this problem without using an extra
# Set or another array for storing all present numbers.
#
# We can use the given nums array itself to mark
# which numbers are present.
#
# For a number x:
#
#     Corresponding index = x - 1
#
# We make nums[x - 1] negative.
#
# This negative value means:
#
#     "Number x is present in the array."
#
# After processing all numbers:
#
#     If nums[i] is positive,
#     then number i + 1 is missing.
#
#
# Example:
#
#     nums = [4,3,2,7,8,2,3,1]
#
#     n = 8
#
# Numbers that should be present:
#
#     1 2 3 4 5 6 7 8
#
# After marking the present numbers, the indices
# corresponding to 5 and 6 remain positive.
#
# Therefore:
#
#     5 and 6 are missing.
#
#
# 🔄 ALGORITHM
#
# 1. Traverse the nums array.
#
# 2. For every element:
#
#       value = abs(nums[i])
#
#    We use abs() because the element may already
#    have been made negative.
#
# 3. Find the corresponding index:
#
#       index = value - 1
#
# 4. Make nums[index] negative:
#
#       nums[index] = -abs(nums[index])
#
#    This marks that the number 'value' is present.
#
# 5. After processing all elements, traverse the array again.
#
# 6. If nums[i] is positive:
#
#       i + 1
#
#    is missing.
#
# 7. Add every missing number to the result.
#
# 8. Return the result.
#
#
# ⭐ WHY DO WE USE abs()?
#
# Suppose an element is already negative because
# another number marked that position.
#
# Example:
#
#     nums[i] = -3
#
# We still need the original value 3.
#
# Therefore:
#
#     abs(-3) = 3
#
# This gives us the original number.
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # Mark every number that is present.
        # We use the input array itself.
        for i in range(len(nums)):

            # Get the original value.
            #
            # The value may already be negative,
            # so use abs() to get the original number.
            value = abs(nums[i])

            # Convert the number into its corresponding index.
            #
            # Number 1 -> index 0
            # Number 2 -> index 1
            # Number 3 -> index 2
            # ...
            index = value - 1

            # Mark this number as present by making
            # the corresponding element negative.
            nums[index] = -abs(nums[index])

        # Store all missing numbers.
        result = []

        # Check every index after marking.
        for i in range(len(nums)):

            # If the value is still positive,
            # the corresponding number is missing.
            if nums[i] > 0:

                # Index i represents number i + 1.
                result.append(i + 1)

        # Return all missing numbers.
        return result


# 🧪 DRY RUN
#
# Input:
#
#     nums = [4,3,2,7,8,2,3,1]
#
# Here:
#
#     n = 8
#
# Therefore, the numbers should be:
#
#     1 2 3 4 5 6 7 8
#
#
# After marking all present numbers:
#
#     [-4,-3,-2,-7,-8,2,-3,-1]
#
#
# Now check each index:
#
#     index 0 -> negative -> number 1 exists
#     index 1 -> negative -> number 2 exists
#     index 2 -> negative -> number 3 exists
#     index 3 -> negative -> number 4 exists
#     index 4 -> negative -> number 5 exists
#     index 5 -> positive -> number 6 is missing
#     index 6 -> negative -> number 7 exists
#     index 7 -> negative -> number 8 exists
#
#
# Therefore:
#
#     result = [5, 6]
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "Since every number is in the range from 1 to n,
# I can use the array indices to mark which numbers
# are present.
#
# For every value, I take value - 1 as its corresponding
# index and make that element negative.
#
# After processing the entire array, if an index still
# contains a positive value, its corresponding number
# is missing.
#
# This solution runs in O(n) time and uses O(1) extra
# space, excluding the returned result."
#
#
# ⭐ KEY POINT TO REMEMBER
#
# Number x corresponds to index:
#
#     x - 1
#
# Present number:
#
#     nums[x - 1] < 0
#
# Missing number:
#
#     nums[x - 1] > 0
#
#
# ⏱️ COMPLEXITY
#
# Time Complexity:
#
#     O(n)
#
# We traverse the array twice.
#
#
# Extra Space Complexity:
#
#     O(1)
#
# We do not use an additional Set, Dictionary,
# or array for marking numbers.
#
#
# Result Space:
#
#     O(k)
#
# where k is the number of missing numbers.
#
# The returned result does not count as extra space
# according to the problem's follow-up.