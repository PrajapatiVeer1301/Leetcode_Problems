# 💡 Simple Logic
#
# In this problem, n <= 10^5.
#
# Numbers from 1 to 999 contain 0 commas.
#
# Every number from 1000 to n contains exactly 1 comma.
#
# Therefore, we only need to count how many numbers are present
# from 1000 to n.
#
# If:
#
# n < 1000
#
# then the answer is 0.
#
# If:
#
# n >= 1000
#
# then the number of values from 1000 to n is:
#
# n - 1000 + 1
#
# which is equal to:
#
# n - 999
#
#
# Example:
#
# n = 1002
#
# Numbers with commas:
#
# 1000 -> 1 comma
# 1001 -> 1 comma
# 1002 -> 1 comma
#
# Total = 3
#
# Formula:
#
# 1002 - 999 = 3


# 🔄 Algorithm
#
# 1. Check whether n is less than 1000.
#
# 2. If n is less than 1000, return 0.
#
# 3. Otherwise, calculate the number of integers from 1000 to n:
#
#       n - 1000 + 1
#
# 4. Return the result.
#
# We can simplify the formula to:
#
#       n - 999
#
# Or directly use:
#
#       max(0, n - 999)
#
# The max function makes sure that the answer never becomes negative.


# 🧪 Dry Run
#
# Example 1:
#
# n = 1002
#
# Numbers from 1 to 999:
# No commas.
#
# Numbers from 1000 to 1002:
#
# 1000 -> 1 comma
# 1001 -> 1 comma
# 1002 -> 1 comma
#
# Number of such values:
#
# 1002 - 1000 + 1 = 3
#
# Answer = 3
#
#
# Example 2:
#
# n = 998
#
# All numbers from 1 to 998 have at most 3 digits.
#
# Therefore, no commas are used.
#
# Answer = 0
#
#
# Example 3:
#
# n = 5000
#
# Every number from 1000 to 5000 contains exactly one comma.
#
# Number of values:
#
# 5000 - 1000 + 1 = 4001
#
# Answer = 4001


# 🎯 Interview Explanation
#
# "The key observation is that the given constraint is n <= 10^5.
#
# Every number from 1 to 999 has fewer than four digits,
# so these numbers contain no commas.
#
# Starting from 1000, every number up to 10^5 contains exactly
# one comma.
#
# Therefore, instead of checking every number individually,
# I simply count the numbers from 1000 to n.
#
# The count is n - 1000 + 1, which simplifies to n - 999.
#
# I use max(0, n - 999) so that the answer is 0 when n is less than 1000."


# ⭐ Key Trick
#
# The most important observation is:
#
# 1 to 999     -> 0 commas
# 1000 to 99999 -> 1 comma each
# 100000       -> 2 commas
#
# IMPORTANT:
#
# Since n can be 100000, the number 100000 contains 2 commas:
#
# 100,000
#
# Therefore, for n = 100000, we must count one extra comma.
#
# So the complete logic is:
#
# - Count all numbers from 1000 to n -> 1 comma each.
# - If n >= 100000, add 1 extra comma for 100000.


# ⏱️ Complexity
#
# Time Complexity: O(1)
#
# We do not iterate through all numbers.
# We only perform a few calculations.
#
#
# Space Complexity: O(1)
#
# We use only a constant amount of extra space.


# 🧑‍💻 Python Code

class Solution:
    def countCommas(self, n: int) -> int:

        # Numbers from 1 to 999 have no commas.
        # Every number from 1000 to n has exactly one comma
        # because n <= 100000.
        
        # Number of integers from 1000 to n:
        # n - 1000 + 1 = n - 999
        
        return max(0, n - 999)





