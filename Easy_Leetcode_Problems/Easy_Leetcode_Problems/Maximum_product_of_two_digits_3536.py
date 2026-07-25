# Logic:
#
# 1. Convert the number into a string.
#
# 2. Store every digit in a list.
#
# 3. Check every pair of digits.
#
# 4. Calculate their product.
#
# 5. Keep updating the maximum product.
#
# 6. Return the maximum product.

# Algorithm:
#
# 1. Convert n into a string.
#
# 2. Convert each character into an integer.
#
# 3. Store all digits in a list.
#
# 4. Initialize maxProduct = 0.
#
# 5. Use two loops to check every pair.
#
# 6. Compute:
#       product = digits[i] * digits[j]
#
# 7. Update maxProduct if needed.
#
# 8. Return maxProduct.

class Solution:
    def maxProduct(self, n: int) -> int:

        digits = [int(d) for d in str(n)]

        maximum = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                maximum = max(maximum, digits[i] * digits[j])

        return maximum

# Interview Explanation:
#
# 1. I converted the number into a list of digits.
#
# 2. I used two nested loops to check every
#    possible pair of digits.
#
# 3. For each pair, I calculated the product
#    and kept track of the maximum value.
#
# 4. Finally, I returned the maximum product.
#
# Time Complexity: O(d²)
# Space Complexity: O(d)
#
# where d is the number of digits in n.