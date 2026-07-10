# Logic:
#
# 1. Use Backtracking (DFS).
#
# 2. Start with an empty combination.
#
# 3. At each step, choose a number.
#
# 4. Add it to the current combination.
#
# 5. Reduce the target by that number.
#
# 6. Since a number can be used multiple times,
#    call recursion with the same index.
#
# 7. If target becomes 0,
#    save the current combination.
#
# 8. If target becomes negative,
#    stop exploring that path.
#
# 9. Backtrack by removing the last number.

# Algorithm:
#
# 1. Create an empty result list.
#
# 2. Create a recursive function.
#
# 3. If target == 0,
#    add the current combination to the result.
#
# 4. If target < 0,
#    return.
#
# 5. Traverse candidates from the current index.
#
# 6. Add the current candidate.
#
# 7. Call recursion with the same index.
#
# 8. Remove the last element (Backtrack).
#
# 9. Return the result.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, target, path):

            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])

        return result
    
# Interview Explanation:
#
# 1. I solved this problem using Backtracking.
#
# 2. At each step, I choose one candidate
#    and subtract it from the target.
#
# 3. Since a number can be reused,
#    I continue recursion from the same index.
#
# 4. If the target becomes 0,
#    I store the current combination.
#
# 5. If the target becomes negative,
#    I stop exploring that path.
#
# 6. After every recursive call,
#    I remove the last element to try other combinations.
#
# Time Complexity: O(2^Target) (approximately)
# Space Complexity: O(Target)