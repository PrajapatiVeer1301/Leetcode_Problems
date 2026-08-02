// Logic:
//
// 1. The number of piles is always even.
//
// 2. The total number of stones
//    is always odd.
//
// 3. Alice always plays first.
//
// 4. Alice can always choose a
//    winning strategy.
//
// 5. Therefore, Alice always wins.
//
// 6. Return true.

// Algorithm:
//
// 1. Read the piles array.
//
// 2. According to the given
//    constraints, Alice always
//    has a winning strategy.
//
// 3. Return true.

// Dry Run:
//
// Input:
//
// piles = [5,3,4,5]
//
// Alice starts first.
//
// Since the number of piles
// is even, Alice can always
// choose a winning strategy.
//
// Therefore,
//
// Return true.

class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}

// Interview Explanation:
//
// 1. This problem has a mathematical
//    observation.
//
// 2. Since the number of piles is
//    always even and the total number
//    of stones is odd, Alice can
//    always force a win.
//
// 3. Therefore, there is no need to
//    simulate the game or use
//    Dynamic Programming.
//
// 4. We simply return true.
//
// Time Complexity: O(1)
//
// Space Complexity: O(1)