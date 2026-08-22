# ---------- 💡 Logic ----------

# 1. Store the original number.
#
#       original_n = n
#
# 2. Initialize:
#
#       digit_sum = 0
#       digit_product = 1
#
# 3. Extract each digit using:
#
#       digit = n % 10
#
# 4. Add the digit to digit_sum.
#
# 5. Multiply the digit with digit_product.
#
# 6. Remove the last digit:
#
#       n = n // 10
#
# 7. Calculate:
#
#       divisor = digit_sum + digit_product
#
# 8. Check:
#
#       original_n % divisor == 0
#
# 9. If remainder is 0 → return True.
#    Otherwise → return False.


# ---------- 🔄 Algorithm ----------

# Step 1: Store the original value of n.
#
# Step 2: Set digit_sum = 0.
#
# Step 3: Set digit_product = 1.
#
# Step 4: While n > 0:
#
#         digit = n % 10
#
#         digit_sum = digit_sum + digit
#
#         digit_product = digit_product * digit
#
#         n = n // 10
#
# Step 5: Calculate:
#
#         divisor = digit_sum + digit_product
#
# Step 6: Check:
#
#         original_n % divisor == 0
#
# Step 7: Return True if divisible,
#         otherwise return False.


# ---------- 🧪 Dry Run ----------

# Input:
# n = 99
#
# --------------------------------
#
# original_n = 99
# digit_sum = 0
# digit_product = 1
#
# --------------------------------
#
# First digit:
#
# digit = 99 % 10
#       = 9
#
# digit_sum = 0 + 9
#           = 9
#
# digit_product = 1 * 9
#               = 9
#
# n = 99 // 10
#   = 9
#
# --------------------------------
#
# Second digit:
#
# digit = 9 % 10
#       = 9
#
# digit_sum = 9 + 9
#           = 18
#
# digit_product = 9 * 9
#               = 81
#
# n = 9 // 10
#   = 0
#
# --------------------------------
#
# divisor = digit_sum + digit_product
#
# divisor = 18 + 81
#         = 99
#
# --------------------------------
#
# Check:
#
# original_n % divisor
#
# 99 % 99 = 0
#
# Therefore:
#
# Output = True


class Solution:
    def checkDivisibility(self, n: int) -> bool:

        original_n = n

        digit_sum = 0
        digit_product = 1

        while n > 0:

            digit = n % 10

            digit_sum += digit
            digit_product *= digit

            n //= 10

        divisor = digit_sum + digit_product

        return original_n % divisor == 0

# ---------- 🎯 Interview Explanation ----------

# I first store the original number because
# n is modified while extracting its digits.
#
# I calculate the digit sum and digit product
# by processing each digit one by one.
#
# I get the last digit using n % 10
# and remove the last digit using n // 10.
#
# Finally, I calculate the sum of digit_sum
# and digit_product.
#
# If the original number is divisible by this
# value, I return True; otherwise, I return False.
#
# Time Complexity: O(log n)
#
# Space Complexity: O(1)


# ---------- ⭐ Key Trick ----------

# digit = n % 10
# → Gets the last digit.
#
# n = n // 10
# → Removes the last digit.
#
# divisor = digit_sum + digit_product
#
# Answer:
#
# original_n % divisor == 0


# ---------- Example ----------

# n = 23
#
# digit_sum = 2 + 3 = 5
#
# digit_product = 2 * 3 = 6
#
# divisor = 5 + 6 = 11
#
# 23 % 11 = 1
#
# Therefore → False