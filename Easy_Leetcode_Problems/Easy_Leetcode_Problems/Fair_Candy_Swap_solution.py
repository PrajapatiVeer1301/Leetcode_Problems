
# ------------------------------------------------------------
# Problem: Fair Candy Swap (LeetCode 888)
# ------------------------------------------------------------

# Algorithm:
# 1. Calculate the total candies of Alice and Bob.
# 2. Find the difference between their totals and divide it by 2.
# 3. Store Bob's candy box sizes in a set.
# 4. Traverse each candy box of Alice.
# 5. Check if Bob has a candy box equal to (Alice's box + difference).
# 6. If found, return the pair.

# Logic:
# Let Alice's total candies = A
# Let Bob's total candies = B
#
# After swapping:
# Alice = A - x + y
# Bob   = B - y + x
#
# For both totals to become equal:
# A - x + y = B - y + x
#
# Therefore:
# y = x + (B - A) // 2
#
# Store Bob's candy boxes in a set for O(1) lookup.
# For every candy box x in Alice's array, check whether
# x + difference exists in Bob's set.
# Return the first valid pair.

# Time Complexity: O(n + m)
# Space Complexity: O(m)


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        diff = (bob_sum - alice_sum) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            y = x + diff
            if y in bob_set:
                return [x, y]
            


# Interview Explanation (1 Minute)

# 1. Calculate the total number of candies Alice and Bob have.
# 2. Compute half of the difference between their total candies.
# 3. If Alice gives a box with x candies, Bob must give a box with
#    x + diff candies so that both have equal candies after swapping.
# 4. Store all of Bob's candy box sizes in a set for O(1) lookup.
# 5. Iterate through Alice's candy boxes and check whether
#    x + diff exists in Bob's set.
# 6. Return the first valid pair found.

# Time Complexity: O(n + m)
# Space Complexity: O(m)