# 💡 LOGIC
#
# We need to check whether the binary representation
# of a positive integer has alternating bits.
#
# Alternating bits means every two adjacent bits
# must be different.
#
# Example:
#
# 5 = 101
#
# The bits are:
#
# 1 -> 0 -> 1
#
# Every adjacent bit is different, so the answer is True.
#
#
# We can check the last bit using:
#
#     n & 1
#
# This gives the rightmost bit of n.
#
# Then we use:
#
#     n >>= 1
#
# to move to the next bit.
#
# If the current bit and previous bit are the same,
# the binary representation does not have alternating bits.
#
#
# ⭐ KEY TRICK — BIT MANIPULATION
#
# Get the last bit:
#
#     n & 1
#
# Move to the next bit:
#
#     n >>= 1
#
#
# 🔄 ALGORITHM
#
# 1. Get the first/rightmost bit using:
#       previous = n & 1
#
# 2. Right shift n by one position:
#       n >>= 1
#
# 3. While n is greater than 0:
#
#       Get the current bit using:
#           current = n & 1
#
#       Compare current with previous.
#
# 4. If current == previous:
#       Return False
#
# 5. Otherwise, update:
#       previous = current
#
# 6. Right shift n again.
#
# 7. If all adjacent bits are different:
#       Return True
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        # Store the previous/rightmost bit
        previous = n & 1

        # Move to the next bit
        n >>= 1

        # Check all remaining bits
        while n > 0:

            # Get the current bit
            current = n & 1

            # If two adjacent bits are the same,
            # the bits are not alternating
            if current == previous:
                return False

            # Update the previous bit
            previous = current

            # Move to the next bit
            n >>= 1

        # All adjacent bits are different
        return True


# 🧪 DRY RUN
#
# Example:
#
# n = 5
#
# Binary representation:
#
#     5 = 101
#
#
# First bit:
#
#     5 & 1 = 1
#
# Therefore:
#
#     previous = 1
#
#
# Shift right:
#
#     101 >> 1 = 10
#
#
# Get the next bit:
#
#     10 & 1 = 0
#
# Compare:
#
#     0 != 1
#
# So the bits are alternating.
#
#
# Shift again:
#
#     10 >> 1 = 1
#
#
# Get the next bit:
#
#     1 & 1 = 1
#
# Compare:
#
#     1 != 0
#
# So the bits are still alternating.
#
#
# No equal adjacent bits were found.
#
# Therefore:
#
#     Answer = True
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I check the binary representation bit by bit using
# bit manipulation.
#
# I store the previous bit using n & 1 and then right
# shift the number to examine the next bit.
#
# For every bit, I compare it with the previous bit.
# If two adjacent bits are equal, I immediately return
# False.
#
# If all adjacent bits are different, I return True.
#
# This solution uses bit manipulation and does not require
# converting the number into a binary string."
#
#
# ⏱️ COMPLEXITY
#
# Time Complexity: O(log n)
#
# We process each bit of the binary representation once.
#
#
# Space Complexity: O(1)
#
# We only use a few variables and no extra data structure.