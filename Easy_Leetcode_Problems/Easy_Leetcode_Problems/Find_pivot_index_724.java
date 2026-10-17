class Solution {
    public int pivotIndex(int[] nums) {

        // ## Main Logic:
        // ## Calculate the total sum of all elements.
        // ## Maintain leftSum, the sum of elements to the left of the current index.
        // ## Calculate rightSum = total - leftSum - nums[i].
        // ## If leftSum == rightSum, the current index is the pivot index.
        // ## Traverse from left to right to find the leftmost pivot index.

        int total = 0;

        // ## Step 1: Calculate the total sum of the array.
        for (int num : nums) {
            total += num;
        }

        // ## Step 2: Initialize the left sum to zero.
        int leftSum = 0;

        // ## Step 3: Check each index.
        for (int i = 0; i < nums.length; i++) {

            // ## Calculate the sum of elements to the right.
            int rightSum = total - leftSum - nums[i];

            // ## If left and right sums are equal, return the index.
            if (leftSum == rightSum) {
                return i;
            }

            // ## Add the current element to the left sum for the next index.
            leftSum += nums[i];
        }

        // ## If no pivot index exists, return -1.
        return -1;
    }
}

/*
## Example:
## Input: nums = [1, 7, 3, 6, 5, 6]
## Total sum = 28

## Dry Run:
## Index 0: Left Sum = 0,  Right Sum = 27
## Index 1: Left Sum = 1,  Right Sum = 20
## Index 2: Left Sum = 8,  Right Sum = 17
## Index 3: Left Sum = 11, Right Sum = 11
## Left Sum equals Right Sum, so return 3.

## Interview Explanation:
## First, calculate the total sum of the array.
## Then, traverse the array while maintaining the left sum.
## Calculate the right sum by subtracting the left sum and current element
## from the total sum.
## If both sums are equal, return the current index.
## If no such index exists, return -1.

## Key Trick:
## rightSum = total - leftSum - nums[i]

## Time Complexity: O(n)
## We traverse the array a constant number of times.

## Space Complexity: O(1)
## We use only a few extra variables.
*/