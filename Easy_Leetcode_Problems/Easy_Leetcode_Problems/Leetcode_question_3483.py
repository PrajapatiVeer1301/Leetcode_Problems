# 💡 Logic
#
# We need to create three-digit even numbers:
#
# Hundreds → Tens → Units
#
# Rules:
#
# 1. The hundreds digit cannot be 0.
# 2. The tens digit can be any available digit.
# 3. The units digit must be even.
# 4. The same array index cannot be used more than once
#    for the same number.
# 5. The same number should be counted only once.
#
# We use three different indices:
#
# i != j
# i != k
# j != k
#
# We create the number using:
#
# number = digits[i] * 100 + digits[j] * 10 + digits[k]
#
# We store every valid number in a set.
#
# A set automatically removes duplicate numbers.


# 🔄 Algorithm
#
# 1. Create an empty set called numbers.
#
# 2. Choose a digit for the hundreds position.
#
# 3. If the hundreds digit is 0, skip it.
#
# 4. Choose a digit for the tens position.
#
# 5. Make sure the tens digit uses a different index.
#
# 6. Choose a digit for the units position.
#
# 7. Make sure the units digit uses a different index
#    from both the hundreds and tens positions.
#
# 8. Check whether the units digit is even.
#
# 9. Create the three-digit number.
#
# 10. Add the number to the set.
#
# 11. After checking all possibilities, return the size of the set.


# 🧪 Dry Run
#
# Example:
#
# digits = [1, 2, 3, 4]
#
# The last digit must be even.
#
# Even digits available:
#
# 2, 4
#
# Some valid numbers are:
#
# 124
# 132
# 134
# 142
# 214
# 234
# 312
# 314
# 324
# 342
# 412
# 432
#
# Total distinct numbers:
#
# 12
#
# Answer = 12


# Example 2:
#
# digits = [0, 2, 2]
#
# Possible valid numbers:
#
# 202
# 220
#
# 022 is not valid because a three-digit number
# cannot start with 0.
#
# Answer = 2


# 🎯 Interview Explanation
#
# "I need to form distinct three-digit even numbers
# using the given digits.
#
# I use three nested loops to choose the hundreds,
# tens, and units digits.
#
# I make sure that the three selected indices are different,
# so each copy of a digit can be used at most once.
#
# The hundreds digit cannot be zero, and the units digit
# must be even.
#
# I store every valid number in a set so that duplicate
# numbers are counted only once.
#
# Finally, I return the size of the set."


# ⭐ Key Trick
#
# The most important trick is using a set:
#
# numbers.add(number)
#
# This handles duplicate digits in the input.
#
# For example:
#
# digits = [2, 2, 4]
#
# The number 224 can be created using different copies
# of the digit 2.
#
# But 224 should be counted only once.
#
# The set automatically removes such duplicates.


# ⏱️ Complexity
#
# Let n be the length of the digits array.
#
# We use three nested loops, so:
#
# Time Complexity: O(n^3)
#
# Since n <= 10, at most 10^3 = 1000 combinations
# are checked.
#
#
# Space Complexity: O(k)
#
# k is the number of distinct valid three-digit numbers.
#
# At most 900 different three-digit even numbers can exist.


# 🧑‍💻 Python Code

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        # Store all distinct valid numbers
        numbers = set()

        # Choose the hundreds digit
        for i in range(len(digits)):

            # A three-digit number cannot start with 0
            if digits[i] == 0:
                continue

            # Choose the tens digit
            for j in range(len(digits)):

                # The same array index cannot be reused
                if i == j:
                    continue

                # Choose the units digit
                for k in range(len(digits)):

                    # The same array index cannot be reused
                    if i == k or j == k:
                        continue

                    # The last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    # Create the three-digit number
                    number = digits[i] * 100 + digits[j] * 10 + digits[k]

                    # Add the number to the set
                    # so duplicate numbers are counted only once
                    numbers.add(number)

        # Return the number of distinct valid numbers
        return len(numbers)