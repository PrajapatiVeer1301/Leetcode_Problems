// Logic:
//
// 1. Find the smallest and
//    largest numbers in the array.
//
// 2. Store all elements in
//    a HashSet.
//
// 3. Traverse every number
//    from smallest to largest.
//
// 4. If a number is not found
//    in the HashSet,
//    it is missing.
//
// 5. Add it to the answer list.
//
// 6. Return the answer.

// Algorithm:
//
// 1. Find the minimum
//    and maximum values.
//
// 2. Store all elements
//    in a HashSet.
//
// 3. Create an empty list.
//
// 4. Traverse from
//    minimum to maximum.
//
// 5. If the current number
//    is not present in
//    the HashSet,
//    add it to the answer.
//
// 6. Return the answer list.

// Dry Run:
//
// Input:
//
// nums = [1,4,2,5]
//
// start = 1
// end = 5
//
// HashSet:
//
// {1,2,4,5}
//
// answer = []
//
// ----------------------
//
// i = 1
//
// Present
//
// answer = []
//
// ----------------------
//
// i = 2
//
// Present
//
// answer = []
//
// ----------------------
//
// i = 3
//
// Missing
//
// answer = [3]
//
// ----------------------
//
// i = 4
//
// Present
//
// answer = [3]
//
// ----------------------
//
// i = 5
//
// Present
//
// answer = [3]
//
// ----------------------
//
// Final Answer:
//
// [3]

import java.util.*;

class Solution {
    public List<Integer> findMissingElements(int[] nums) {

        int start = nums[0];
        int end = nums[0];

        // Find minimum and maximum
        for (int num : nums) {
            if (num < start)
                start = num;

            if (num > end)
                end = num;
        }

        // Store elements in HashSet
        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        // Find missing numbers
        List<Integer> answer = new ArrayList<>();

        for (int i = start; i <= end; i++) {

            if (!set.contains(i)) {
                answer.add(i);
            }
        }

        return answer;
    }
}

// Interview Explanation:
//
// 1. I first found the minimum
//    and maximum values in the array.
//
// 2. Then I stored all elements
//    in a HashSet to get O(1)
//    lookup time.
//
// 3. I traversed every number
//    between the minimum and
//    maximum values.
//
// 4. If a number was not found
//    in the HashSet,
//    I added it to the answer.
//
// 5. Finally, I returned the
//    list of missing numbers.
//
// Time Complexity: O(n + range)
//
// Space Complexity: O(n)