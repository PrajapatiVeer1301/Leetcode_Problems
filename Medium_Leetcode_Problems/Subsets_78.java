// Logic:
//
// 1. Use Backtracking to generate all subsets.
//
// 2. For every element, there are two choices:
//
//      - Take the element
//      - Do not take the element
//
// 3. Add the current subset to the result.
//
// 4. Add an element to current.
//
// 5. Recursively process the remaining elements.
//
// 6. Remove the element using backtracking.
//
// Example:
//
// nums = [1,2,3]
//
// Start with:
// []
//
// Choose 1:
// [1]
//
// Choose 2:
// [1,2]
//
// Choose 3:
// [1,2,3]
//
// Then backtrack and try other combinations.

// Algorithm:
//
// 1. Create result list.
//
// 2. Create an empty current subset.
//
// 3. Call backtrack(nums, 0, current, result).
//
// 4. Add current subset to result.
//
// 5. Loop from index to nums.length:
//
//      Add nums[i] to current.
//
//      Call backtrack(i + 1).
//
//      Remove nums[i] from current.
//
// 6. Return result.

// Dry Run:
//
// nums = [1,2,3]
//
// Start:
//
// current = []
// result = [[]]
//
// -------------------------
//
// Choose 1
//
// current = [1]
// result = [[], [1]]
//
// Choose 2
//
// current = [1,2]
//
// Choose 3
//
// current = [1,2,3]
//
// result contains:
// [1,2,3]
//
// -------------------------
//
// Backtrack:
//
// Remove 3
// current = [1,2]
//
// Remove 2
// current = [1]
//
// Choose 3
//
// current = [1,3]
//
// result contains:
// [1,3]
//
// -------------------------
//
// Backtrack:
//
// Remove 3
// Remove 1
//
// current = []
//
// Choose 2
//
// current = [2]
//
// Choose 3
//
// current = [2,3]
//
// result contains:
// [2,3]
//
// -------------------------
//
// Backtrack:
//
// Remove 3
// Remove 2
//
// Choose 3
//
// current = [3]
//
// result contains:
// [3]
//
// -------------------------
//
// Final Result:
//
// [[], [1], [1,2], [1,2,3],
//  [1,3], [2], [2,3], [3]]

//Choose
//   ↓
//Recursive Call
//   ↓
//Backtrack

import java.util.*;

class Solution {

    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        backtrack(nums, 0, current, result);

        return result;
    }

    private void backtrack(int[] nums, int index,
                            List<Integer> current,
                            List<List<Integer>> result) {

        // Add current subset
        result.add(new ArrayList<>(current));

        // Try every remaining element
        for (int i = index; i < nums.length; i++) {

            // Choose
            current.add(nums[i]);

            // Explore
            backtrack(nums, i + 1, current, result);

            // Backtrack
            current.remove(current.size() - 1);
        }
    }
}

// Interview Explanation:
//
// I used Backtracking to generate
// all possible subsets.
//
// For every element, I add it to
// the current subset and recursively
// generate subsets using the remaining
// elements.
//
// After the recursive call, I remove
// the element to try another possibility.
//
// I add the current subset before
// exploring further because every
// current state is a valid subset.
//
// Since every element has two choices,
// include or exclude, there are 2^n
// possible subsets.
//
// Time Complexity: O(n * 2^n)
//
// Space Complexity: O(n)
// excluding the output.


//   ⭐ Remember
current.add(nums[i]);              // Choose
backtrack(nums, i + 1, current, result); // Explore
current.remove(current.size() - 1);       // Backtrack