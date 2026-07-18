// Logic:
//
// 1. Find the smallest element in the array.
//
// 2. Find the largest element in the array.
//
// 3. Use the Euclidean Algorithm to find
//    the GCD of the smallest and largest.
//
// 4. Return the GCD.

// Algorithm:
//
// 1. Initialize small and large with nums[0].
//
// 2. Traverse the array to find the minimum
//    and maximum values.
//
// 3. Apply the Euclidean Algorithm:
//
//    while (large != 0)
//        remainder = small % large
//        small = large
//        large = remainder
//
// 4. Return small as the GCD.


class Solution {
    public int findGCD(int[] nums) {

        int small = nums[0];
        int large = nums[0];

        // Find smallest and largest
        for (int num : nums) {
            if (num < small) {
                small = num;
            }
            if (num > large) {
                large = num;
            }
        }

        // Find GCD using Euclidean Algorithm
        while (large != 0) {
            int temp = large;
            large = small % large;
            small = temp;
        }

        return small;
    }
}

// Interview Explanation:
//
// 1. First, I traversed the array to find
//    the smallest and largest elements.
//
// 2. Then I used the Euclidean Algorithm
//    to compute their GCD.
//
// 3. The algorithm repeatedly replaces
//    the larger number with the remainder
//    until the remainder becomes zero.
//
// 4. The remaining number is the GCD.
//
// Time Complexity: O(n + log(max))
// Space Complexity: O(1)


