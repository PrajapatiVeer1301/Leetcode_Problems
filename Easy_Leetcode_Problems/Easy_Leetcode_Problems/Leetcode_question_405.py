# 💡 Logic
#
# We need to convert a 32-bit integer into its hexadecimal representation
# without using Python's built-in hex() function.
#
# Hexadecimal uses 16 symbols:
#
# 0 1 2 3 4 5 6 7 8 9 a b c d e f
#
# ⭐ Key Trick
#
# Each hexadecimal digit represents exactly 4 binary bits.
#
# To get the last 4 bits of the number, we use:
#
# num & 15
#
# because:
#
# 15 = 1111 in binary
#
# So, num & 15 extracts the last 4 bits.
#
# Then we move to the next 4 bits using:
#
# num >>= 4
#
# This process continues until num becomes 0.
#
# For negative numbers, we need 32-bit two's complement.
# We can force the number to behave like a 32-bit unsigned value using:
#
# num &= 0xFFFFFFFF
#
# 0xFFFFFFFF represents 32 bits containing all 1s.
#
#
# 🔄 Algorithm
#
# 1. If num == 0, return "0".
#
# 2. Convert the number to its 32-bit representation using:
#    num &= 0xFFFFFFFF
#
# 3. Create a string containing all hexadecimal digits:
#
#    hex_chars = "0123456789abcdef"
#
# 4. While num > 0:
#
#    - Get the last 4 bits using num & 15.
#    - Use that value as an index in hex_chars.
#    - Add the hexadecimal character to result.
#    - Shift num right by 4 bits.
#
# 5. The digits are generated from right to left,
#    so reverse the result.
#
# 6. Return the final hexadecimal string.
#
#
# 🧑‍💻 Python Code

class Solution:
    def toHex(self, num: int) -> str:

        # If the number is 0, return "0"
        if num == 0:
            return "0"

        # Convert negative number into 32-bit two's complement
        num &= 0xFFFFFFFF

        # Store all hexadecimal digits
        hex_chars = "0123456789abcdef"

        # Store the hexadecimal result
        result = ""

        # Process 4 bits at a time
        while num > 0:

            # Get the last 4 bits
            digit = num & 15

            # Convert the digit into a hexadecimal character
            result += hex_chars[digit]

            # Move to the next 4 bits
            num >>= 4

        # Digits were generated from right to left,
        # so reverse the result
        return result[::-1]


# 🧪 Dry Run: num = 26
#
# Binary representation:
#
# 26 = 11010
#
# First iteration:
#
# 26 & 15 = 10
#
# Hexadecimal value of 10 = 'a'
#
# result = "a"
#
# Now shift right by 4:
#
# 26 >> 4 = 1
#
# Second iteration:
#
# 1 & 15 = 1
#
# Hexadecimal value of 1 = '1'
#
# result = "a1"
#
# The digits were generated from right to left.
#
# Reverse:
#
# "a1" → "1a"
#
# ✅ Answer = "1a"
#
#
# 🧪 Negative Example: num = -1
#
# For a 32-bit integer:
#
# -1 is represented using two's complement as:
#
# 11111111 11111111 11111111 11111111
#
# In hexadecimal:
#
# f f f f f f f f
#
# After:
#
# num &= 0xFFFFFFFF
#
# num behaves as:
#
# 0xFFFFFFFF
#
# Every group of 4 bits gives 'f'.
#
# Therefore:
#
# result = "ffffffff"
#
# ✅ Answer = "ffffffff"
#
#
# ⏱️ Complexity
#
# Time Complexity: O(1)
#
# A 32-bit integer has at most 8 hexadecimal digits,
# so the loop runs at most 8 times.
#
# Space Complexity: O(1)
#
# The result contains at most 8 characters.
#
#
# 🎯 Interview Explanation
#
# "I convert the integer to hexadecimal manually using bit operations.
# Since one hexadecimal digit represents 4 bits, I use num & 15
# to extract the last 4 bits and map them to a hexadecimal character.
# Then I shift the number right by 4 bits and repeat the process.
# For negative numbers, I mask the value with 0xFFFFFFFF so that
# it behaves as a 32-bit two's-complement value.
# Since the digits are generated from right to left, I reverse
# the result before returning it."