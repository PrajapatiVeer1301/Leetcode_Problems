// TARGET INDICES AFTER SORTING ARRAY_2089

// ## LOGIC:
        // ## First, sort the array in non-decreasing order.
        // ## Check every index of the sorted array.
        // ## If nums[i] == target, store index i in the result list.
        // ## Traversing from left to right keeps indices in increasing order.
        // ## If the target is not found, return an empty list.

import java.util.*;

class Solution {

    public List<Integer> targetIndices(int[] nums, int target) {

        // ## Step 1: Sort the array in ascending order.
        Arrays.sort(nums);

        // ## Step 2: Create an empty list to store target indices.
        List<Integer> result = new ArrayList<>();

        // ## Step 3: Traverse the sorted array using indices.
        for (int i = 0; i < nums.length; i++) {

            // ## Step 4: Check whether the current element equals target.
            if (nums[i] == target) {

                // ## Step 5: Store the index if the target is found.
                result.add(i);
            }
        }

        // ## Step 6: Return all target indices in increasing order.
        return result;
    }
}

/*
## EXAMPLE:
## Input: nums = [1, 2, 5, 2, 3], target = 2
## After sorting: [1, 2, 2, 3, 5]
## Output: [1, 2]


## DRY RUN:
## Original array: [1, 2, 5, 2, 3]
## Target: 2
##
## Step 1: Sort the array.
## Sorted array = [1, 2, 2, 3, 5]
##
## Step 2: Check each index.
## Index 0, value 1 -> Target not found, ignore.
## Index 1, value 2 -> Target found, add index 1.
## Index 2, value 2 -> Target found, add index 2.
## Index 3, value 3 -> Target not found, ignore.
## Index 4, value 5 -> Target not found, ignore.
##
## Final result = [1, 2]


## ALGORITHM:
## Step 1: Sort nums using Arrays.sort(nums).
## Step 2: Create an empty list named result.
## Step 3: Traverse the array from index 0 to nums.length - 1.
## Step 4: If nums[i] == target, add i to result.
## Step 5: Return result.


## INTERVIEW EXPLANATION:
## First, I sort the given array in non-decreasing order.
## Then, I traverse the sorted array from left to right.
## At each index, I compare the current element with the target.
## If the element equals the target, I add its index to the result.
## If the target occurs multiple times, I collect every matching index.
## Since I traverse in increasing index order, the returned indices
## are already sorted.
## If no element matches the target, the result remains empty.
## Finally, I return the result list.


## KEY TRICK:
## Arrays.sort(nums) sorts the array.
## nums[i] == target checks whether the current element matches.
## result.add(i) stores the index, not the element.
## Traversing from left to right keeps indices in increasing order.


## TIME AND SPACE COMPLEXITY:
## Let n be the number of elements in nums.
##
## Time Complexity: O(n log n)
## Sorting takes O(n log n), and traversal takes O(n).
##
## Auxiliary Space Complexity: O(n) in the worst case.
## The result list can contain up to n indices.
## Sorting may also use implementation-dependent extra space.
*/
