



// Logic:
//
// 1. Use Backtracking to find all possible combinations.
//
// 2. Start with an empty combination.
//
// 3. Add one candidate to the current combination.
//
// 4. Subtract the selected number from the target.
//
// 5. Since a number can be used multiple times,
//    call recursion with the same index.
//
// 6. If target becomes 0,
//    store the current combination.
//
// 7. If target becomes negative,
//    stop exploring that path.
//
// 8. Remove the last element (Backtracking)
//    and try the next candidate.

// Algorithm:
//
// 1. Create an empty result list.
//
// 2. Create a recursive backtracking function.
//
// 3. If target == 0,
//    add the current combination to the result.
//
// 4. If target < 0,
//    return.
//
// 5. Traverse candidates from the current index.
//
// 6. Add the current candidate to the combination.
//
// 7. Call recursion with the same index.
//
// 8. Remove the last element.
//
// 9. Continue until all combinations are explored.
//
// 10. Return the result.

class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> result = new ArrayList<>();

        backtrack(candidates, target, 0, new ArrayList<>(), result);

        return result;
    }

    private void backtrack(int[] candidates, int target, int start,
                           List<Integer> path, List<List<Integer>> result) {

        if (target == 0) {
            result.add(new ArrayList<>(path));
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            backtrack(candidates, target - candidates[i], i, path, result);
            path.remove(path.size() - 1);
        }
    }
}

// Interview Explanation:
//
// 1. I solved this problem using the Backtracking approach.
//
// 2. At each recursive call, I choose one candidate
//    and subtract it from the target.
//
// 3. Since a number can be selected multiple times,
//    I call recursion with the same index.
//
// 4. If the target becomes 0,
//    I save the current combination.
//
// 5. If the target becomes negative,
//    I stop exploring that path.
//
// 6. After every recursive call,
//    I remove the last element to explore other possibilities.
//
// Time Complexity: O(2^Target) (approximately)
// Space Complexity: O(Target)












