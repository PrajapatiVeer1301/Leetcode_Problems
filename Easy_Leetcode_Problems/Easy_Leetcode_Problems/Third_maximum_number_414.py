# 💡 LOGIC
#
# We need to find the third distinct maximum number.
#
# We maintain three variables:
#
# first  -> largest distinct number
# second -> second largest distinct number
# third  -> third largest distinct number
#
# Important:
# Duplicate values should be counted only once.
#
# Example:
#
# nums = [2, 2, 3, 1]
#
# Distinct values are:
# 3, 2, 1
#
# Therefore, the third maximum is 1.
#
#
# 🔄 ALGORITHM
#
# 1. Initialize first, second, and third as None.
#
# 2. Traverse every number in the array.
#
# 3. If the number is already equal to first, second,
#    or third, skip it because it is a duplicate.
#
# 4. If the number is greater than first:
#       Move second to third.
#       Move first to second.
#       Store number in first.
#
# 5. Else if the number is greater than second:
#       Move second to third.
#       Store number in second.
#
# 6. Else if the number is greater than third:
#       Store number in third.
#
# 7. After processing all numbers:
#       If third exists, return third.
#       Otherwise, return first.
#
#
# ⭐ KEY POINT
#
# "Distinct maximum" means duplicate values are counted only once.
#
# Example:
#
# [3, 3, 2, 1]
#
# Distinct values:
#
# [3, 2, 1]
#
# First maximum  = 3
# Second maximum = 2
# Third maximum  = 1
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        # Store the largest distinct value
        first = None

        # Store the second largest distinct value
        second = None

        # Store the third largest distinct value
        third = None

        # Traverse every number in the array
        for num in nums:

            # Ignore duplicate values
            if num == first or num == second or num == third:
                continue

            # If num is the largest value
            if first is None or num > first:

                # Shift the existing values
                third = second
                second = first
                first = num

            # If num is the second largest value
            elif second is None or num > second:

                # Move the old second maximum to third
                third = second
                second = num

            # If num is the third largest value
            elif third is None or num > third:

                # Store num as the third maximum
                third = num

        # If the third distinct maximum exists,
        # return it
        if third is not None:
            return third

        # Otherwise, return the largest value
        return first


# 🧪 DRY RUN
#
# Example:
#
# nums = [2, 2, 3, 1]
#
# Initially:
#
# first = None
# second = None
# third = None
#
#
# Process 2:
#
# 2 is greater than first.
#
# first = 2
# second = None
# third = None
#
#
# Process next 2:
#
# 2 is already equal to first.
#
# Therefore, skip it.
#
#
# Process 3:
#
# 3 > first
#
# Shift the values:
#
# third = second
# second = first
# first = 3
#
# Now:
#
# first = 3
# second = 2
# third = None
#
#
# Process 1:
#
# 1 is not greater than first or second.
#
# Therefore:
#
# third = 1
#
#
# Final:
#
# first = 3
# second = 2
# third = 1
#
# Answer:
#
# 1
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I maintain three variables to store the first, second,
# and third distinct maximum values.
#
# While traversing the array, I ignore duplicate values.
# If the current number is larger than the first maximum,
# I shift the existing values down.
#
# Similarly, if it is larger than the second or third maximum,
# I update the appropriate variable.
#
# At the end, if a third distinct maximum exists, I return it.
# Otherwise, I return the first maximum.
#
# This allows me to solve the problem in one pass without
# sorting the array."
#
#
# ⏱️ COMPLEXITY
#
# Time Complexity: O(n)
#
# We traverse the array only once.
#
# Space Complexity: O(1)
#
# We use only three variables:
#
# first, second, and third.
#
#
# ⭐ IMPORTANT EXAMPLE
#
# nums = [1, 2]
#
# Distinct values:
#
# [2, 1]
#
# There is no third distinct maximum.
#
# Therefore, we return the maximum:
#
# 2