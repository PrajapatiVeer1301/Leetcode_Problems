//---------- 💡 Logic ----------

// We use Backtracking.
//
// current = stores the current combination.
//
// Start from 1.
//
// For every number:
// 1. Add the number.
// 2. Recursively choose the next number.
// 3. Remove the number (backtrack).
//
// When current.size() == k,
// add the combination to result.

// ---------- 🔄 Algorithm ----------

// Step 1: Create an empty result list.
//
// Step 2: Create an empty current list.
//
// Step 3: Create a backtracking function.
//
// Step 4: If current.size() == k:
//         Add a copy of current to result.
//
// Step 5: Run a loop from start to n.
//
// Step 6: Add the current number to current.
//
// Step 7: Recursively call backtracking
//         for the next number.
//
// Step 8: Remove the last number from current
//         to backtrack.
//
// Step 9: Return the result list.

//--------- 🔄 Dry Run ----------


// n = 4, k = 2
//
// Start:
// current = []
//
// Choose 1:
//
// current = [1]
//
// Choose 2:
//
// current = [1,2]
// → size = 2
// → add [1,2]
//
// Backtrack:
//
// current = [1]
//
// Choose 3:
//
// current = [1,3]
// → add [1,3]
//
// Choose 4:
//
// current = [1,4]
// → add [1,4]
//
// Backtrack to:
//
// current = []
//
// Choose 2:
//
// current = [2]
//
// Choose 3:
//
// current = [2,3]
// → add [2,3]
//
// Choose 4:
//
// current = [2,4]
// → add [2,4]
//
// Finally:
//
// [3,4]
//
// Result:
//
// [[1,2], [1,3], [1,4],
//  [2,3], [2,4], [3,4]]


import java.util.*;

class Solution {

    public List<List<Integer>> combine(int n, int k) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        backtrack(1, n, k, current, result);

        return result;
    }

    private void backtrack(int start, int n, int k,
                           List<Integer> current,
                           List<List<Integer>> result) {

        // If k numbers are selected
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Try all numbers from start to n
        for (int i = start; i <= n; i++) {

            // Choose
            current.add(i);

            // Explore
            backtrack(i + 1, n, k, current, result);

            // Backtrack
            current.remove(current.size() - 1);
        }
    }
}

//------- 🎯 Interview Explanation --------

// I use backtracking to generate all combinations.
//
// The current list stores the selected numbers.
//
// I always select the next number from i + 1,
// so the same combination is not generated again
// in a different order.
//
// When k elements are selected, I add a copy
// of current to the result.
//
// After exploring a choice, I remove it and
// try the next choice.
//
// Time Complexity:
// O(C(n,k) * k)
//
// Space Complexity:
// O(k) auxiliary space,
// excluding the output.

//------- ⭐ Key Trick ------

// This line is very important:
//
// backtrack(i + 1, n, k, current, result);
//
// We use i + 1 instead of i.
//
// Therefore:
//
// [1,2] ✅
//
// [2,1] ❌
//
// [1,3] ✅
//
// [3,1] ❌
//
// This prevents duplicate combinations.