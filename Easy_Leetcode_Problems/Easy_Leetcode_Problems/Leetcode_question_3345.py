# Logic:
#
# 1. Start checking from n.
#
# 2. Find the product of
#    all digits.
#
# 3. Check whether the
#    product is divisible
#    by t.
#
# 4. If divisible,
#    return the number.
#
# 5. Otherwise,
#    increase n by 1.
#
# 6. Repeat until
#    the answer is found.

# Algorithm:
#
# 1. Start from n.
#
# 2. Calculate the product
#    of its digits.
#
# 3. If product % t == 0:
#       return n
#
# 4. Otherwise:
#       n = n + 1
#
# 5. Repeat.

# Dry Run:
#
# Input:
#
# n = 15
# t = 3
#
# -------------------
#
# Number = 15
#
# Product:
#
# 1 × 5 = 5
#
# 5 % 3 = 2
#
# Not divisible
#
# n = 16
#
# -------------------
#
# Number = 16
#
# Product:
#
# 1 × 6 = 6
#
# 6 % 3 = 0
#
# Divisible
#
# Return 16

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:

            product = 1

            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1

# Interview Explanation:
#
# 1. I started checking
#    from n.
#
# 2. For every number,
#    I calculated the
#    product of its digits.
#
# 3. If the product was
#    divisible by t,
#    I returned that number.
#
# 4. Otherwise, I checked
#    the next number.
#
# 5. Since n <= 100,
#    this brute-force
#    solution is efficient.
#
# Time Complexity: O(k × d)
#
# where
# k = numbers checked
# d = number of digits
#
# Space Complexity: O(1)

