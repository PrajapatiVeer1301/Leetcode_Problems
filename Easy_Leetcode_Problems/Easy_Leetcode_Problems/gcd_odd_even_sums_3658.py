# Logic:
#
# 1. Sum of first n odd numbers is n².
#
# 2. Sum of first n even numbers is n(n+1).
#
# 3. GCD(n², n(n+1)) is always n.
#
# 4. Return n.

# Algorithm:
#
# 1. Read the input n.
#
# 2. Return n.

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
    # Interview Explanation:
#
# 1. The sum of the first n odd numbers is n².
#
# 2. The sum of the first n even numbers is n(n+1).
#
# 3. The GCD of n² and n(n+1) simplifies to n,
#    because n and n+1 are consecutive numbers
#    and their GCD is always 1.
#
# 4. Therefore, the answer is simply n.
#
# Time Complexity: O(1)
# Space Complexity: O(1)