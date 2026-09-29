# 💡 LOGIC
#
# We need to check whether a given integer n is a power of 2.
#
# Powers of 2 are:
#
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# 2^4 = 16
# ...
#
# A power of 2 has exactly ONE set bit (1)
# in its binary representation.
#
# For example:
#
# 16 = 10000
#  8 = 01000
#  4 = 00100
#
# We can use the special bit manipulation property:
#
#     n & (n - 1) == 0
#
# But n must be positive.
#
#
# ⭐ KEY TRICK — BIT MANIPULATION
#
# For a power of 2:
#
#     n & (n - 1) == 0
#
# Why?
#
# Example: n = 16
#
# Binary:
#
# 16 = 10000
# 15 = 01111
#
# AND:
#
# 10000
# 01111
# -----
# 00000
#
# Therefore, 16 is a power of 2.
#
#
# Example: n = 6
#
# Binary:
#
# 6 = 0110
# 5 = 0101
#
# AND:
#
# 0110
# 0101
# ----
# 0100
#
# The result is not 0.
#
# Therefore, 6 is not a power of 2.
#
#
# 🔄 ALGORITHM
#
# 1. Check if n is less than or equal to 0.
#
# 2. If n <= 0:
#       Return False.
#
# 3. Apply the bit manipulation condition:
#
#       (n & (n - 1)) == 0
#
# 4. If the condition is true:
#       n is a power of 2.
#
# 5. Otherwise:
#       n is not a power of 2.
#
# 6. Return the result.
#
#
# 🧑‍💻 PYTHON CODE

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # n must be positive
        if n <= 0:
            return False

        # A power of two has exactly one set bit.
        #
        # Therefore, n & (n - 1) will be 0
        # only when n is a power of two.
        return (n & (n - 1)) == 0


# 🧪 DRY RUN
#
# Example 1:
#
# n = 16
#
# 16 = 10000
# 15 = 01111
#
# 16 & 15:
#
# 10000
# 01111
# -----
# 00000
#
# Result = 0
#
# Therefore:
#
# True
#
#
# Example 2:
#
# n = 3
#
# 3 = 0011
# 2 = 0010
#
# 3 & 2:
#
# 0011
# 0010
# ----
# 0010
#
# Result is not 0.
#
# Therefore:
#
# False
#
#
# 🎯 INTERVIEW EXPLANATION
#
# "I first check whether n is positive because powers of two
# are always positive.
#
# Then I use the bit manipulation property n & (n - 1).
# A power of two has exactly one set bit in its binary
# representation.
#
# When we subtract 1 from a power of two, that set bit
# becomes 0 and all the lower bits become 1.
#
# Therefore, performing AND between n and n - 1 gives 0
# only when n is a power of two.
#
# This solution does not use any loop or recursion."
#
#
# ⏱️ COMPLEXITY
#
# Time Complexity: O(1)
#
# We perform only a few bit operations.
#
# Space Complexity: O(1)
#
# We use only constant extra space.
#
#
# ⭐ FOLLOW-UP
#
# This solution satisfies the follow-up because it uses:
#
# - No loop
# - No recursion
# - O(1) time
# - O(1) space