# Logic:
#
# 1. Sort the scores in descending order.
#
# 2. Store each score and its rank in a dictionary.
#
# 3. Assign:
#    Rank 1 -> Gold Medal
#    Rank 2 -> Silver Medal
#    Rank 3 -> Bronze Medal
#    Remaining -> Rank number.
#
# 4. Traverse the original array.
#
# 5. Replace each score with its rank.
#
# 6. Return the result.

# Algorithm:
#
# 1. Copy and sort the score array in descending order.
#
# 2. Create a dictionary.
#
# 3. Assign ranks to every score.
#
# 4. Create the answer array.
#
# 5. Traverse the original score array.
#
# 6. Store the corresponding rank.
#
# 7. Return the answer.

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_scores = sorted(score, reverse=True)

        rank = {}

        for i in range(len(sorted_scores)):

            if i == 0:
                rank[sorted_scores[i]] = "Gold Medal"

            elif i == 1:
                rank[sorted_scores[i]] = "Silver Medal"

            elif i == 2:
                rank[sorted_scores[i]] = "Bronze Medal"

            else:
                rank[sorted_scores[i]] = str(i + 1)

        result = []

        for s in score:
            result.append(rank[s])

        return result
    
# Interview Explanation:
#
# 1. I sorted the scores in descending order.
#
# 2. Then I assigned medals to the top three athletes.
#
# 3. For the remaining athletes,
#    I assigned their rank numbers.
#
# 4. I stored the score-to-rank mapping in a dictionary.
#
# 5. Finally, I traversed the original array
#    and replaced each score with its rank.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)