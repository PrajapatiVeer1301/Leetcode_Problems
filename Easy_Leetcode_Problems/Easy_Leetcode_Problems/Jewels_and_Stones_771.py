# Logic:
#
# 1. Store all jewel characters in a set.
#
# 2. Traverse each stone.
#
# 3. Check if the stone exists in the jewel set.
#
# 4. If yes, increase the count.
#
# 5. Return the final count.

# Algorithm:
#
# 1. Convert jewels into a set.
#
# 2. Initialize count = 0.
#
# 3. Traverse every character in stones.
#
# 4. If the character exists in the jewel set,
#    increment count.
#
# 5. Return count.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewel_set = set(jewels)

        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count
    
    # Interview Explanation:
#
# 1. I converted the jewels string into a set for fast lookup.
#
# 2. Then I traversed each stone.
#
# 3. If the current stone exists in the jewel set,
#    I increased the count.
#
# 4. Finally, I returned the total number of jewels.
#
# Time Complexity: O(n)
# Space Complexity: O(m)
#
# where:
# n = length of stones
# m = length of jewels