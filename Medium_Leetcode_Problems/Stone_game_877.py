# Logic:
#
# 1. The number of piles is always even.
#
# 2. The total number of stones is odd,
#    so a tie is impossible.
#
# 3. Alice always moves first.
#
# 4. Alice can always choose a strategy
#    that guarantees more stones than Bob.
#
# 5. Therefore, Alice always wins.
#
# 6. Return True.

# Algorithm:
#
# 1. Read the piles array.
#
# 2. Since Alice always has
#    a winning strategy,
#    return True.

# Dry Run:
#
# Input:
#
# piles = [5,3,4,5]
#
# Alice starts first.
#
# Alice can always choose
# the winning strategy.
#
# Therefore,
#
# Return True.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# Interview Explanation:
#
# 1. This problem has a mathematical
#    observation.
#
# 2. Since the number of piles is
#    always even and the total number
#    of stones is odd,
#    Alice can always force a win.
#
# 3. Therefore, no simulation or
#    dynamic programming is required.
#
# 4. We simply return True.
#
# Time Complexity: O(1)
#
# Space Complexity: O(1)

