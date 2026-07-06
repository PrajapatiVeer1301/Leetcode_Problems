
# Logic:
#
# 1. Find all unique candy types using a set.
#
# 2. Count the number of unique candy types.
#
# 3. Alice can eat only n/2 candies.
#
# 4. The answer is the minimum of:
#    - Number of unique candy types.
#    - n/2.
#
# 5. Return the result.

# Algorithm:
#
# 1. Calculate total number of candies.
#
# 2. Find the number of unique candy types.
#
# 3. Calculate the maximum candies Alice can eat as n/2.
#
# 4. Return min(unique_types, n/2).

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        unique_types = len(set(candyType))

        max_candies = len(candyType) // 2

        return min(unique_types, max_candies)
    
    # Interview Explanation:
#
# 1. First, I find all unique candy types using a set.
#
# 2. Then, I count the number of unique candy types.
#
# 3. Alice can eat only n/2 candies.
#
# 4. Therefore, the answer is the minimum of
#    unique candy types and n/2.
#
# 5. Finally, I return the result.
#
# Time Complexity: O(n)
# Space Complexity: O(n)