# Logic:
#
# 1. Sort all unique elements.
#
# 2. Assign ranks starting from 1.
#
# 3. Store each number and its rank in a dictionary.
#
# 4. Traverse the original array.
#
# 5. Replace each element with its rank.
#
# 6. Return the updated array.


# Algorithm:
#
# 1. Remove duplicate elements using set().
#
# 2. Sort the unique elements.
#
# 3. Create a dictionary to store number → rank.
#
# 4. Start rank from 1.
#
# 5. Traverse the original array.
#
# 6. Replace every element with its rank.
#
# 7. Return the transformed array.


from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted_arr = sorted(set(arr))

        rank = {}

        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1

        return [rank[num] for num in arr]
    

# Interview Explanation:
#
# 1. First, I removed duplicate elements using a set.
#
# 2. Then, I sorted the unique elements.
#
# 3. I assigned ranks starting from 1 using a dictionary.
#
# 4. Finally, I traversed the original array and replaced
#    each element with its corresponding rank.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
