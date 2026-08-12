// Permutation means arranging the same elements
// in different orders.
//
// Example:
//
// [1, 2, 3]
//
// Possible permutations:
//
// [1, 2, 3]
// [1, 3, 2]
// [2, 1, 3]
// [2, 3, 1]
// [3, 1, 2]
// [3, 2, 1]
//
// Important:
// In permutation, ORDER MATTERS.
//
// [1, 2] != [2, 1]
//
// Easy meaning:
// Permutation = Arrangement 


import java.util.*;

class Solution {

    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        boolean[] used = new boolean[nums.length];

        backtrack(nums, current, used, result);

        return result;
    }

    private void backtrack(int[] nums,
                           List<Integer> current,
                           boolean[] used,
                           List<List<Integer>> result) {

        // If permutation is complete
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Try every element
        for (int i = 0; i < nums.length; i++) {

            // Skip already used element
            if (used[i]) {
                continue;
            }

            // Choose
            used[i] = true;
            current.add(nums[i]);

            // Explore
            backtrack(nums, current, used, result);

            // Backtrack
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}


// Interview Explanation:
//
// I used Backtracking to generate all permutations.
//
// For every position, I try every element that
// has not been used yet.
//
// I use a boolean array "used" to keep track
// of the elements already selected.
//
// When the current list reaches the same size
// as the input array, I add it to the result.
//
// After the recursive call, I remove the last
// element and mark it as unused.
//
// This allows us to try all possible arrangements.
//
// Time Complexity: O(n × n!)
//
// Space Complexity: O(n), excluding the output.


// ⭐ Important Lines
used[i] = true;                 // Choose
backtrack(...);                 // Explore
used[i] = false;                // Backtrack


