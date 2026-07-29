# Logic:
#
# 1. Find the maximum number of candies.
#
# 2. Traverse each kid.
#
# 3. Add extraCandies to the current kid.
#
# 4. If the total is greater than or equal
#    to the maximum candies,
#    add True to the answer.
#
# 5. Otherwise, add False.
#
# 6. Return the result list.

# Algorithm:
#
# 1. Find maxCandy = max(candies).
#
# 2. Create an empty result list.
#
# 3. Traverse the candies array.
#
# 4. If:
#
#      candy + extraCandies >= maxCandy
#
#      store True.
#
#    Else
#
#      store False.
#
# 5. Return the result.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandy = max(candies)

        result = []

        for candy in candies:

            if candy + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)

        return result

# Interview Explanation:
#
# 1. I first found the maximum number
#    of candies among all kids.
#
# 2. Then I traversed the array again.
#
# 3. For each kid, I added the extra
#    candies and checked whether the
#    total was greater than or equal
#    to the current maximum.
#
# 4. If yes, I stored True;
#    otherwise, I stored False.
#
# Time Complexity: O(n)
#
# Space Complexity: O(n)