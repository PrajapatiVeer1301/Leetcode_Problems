// Logic:
//
// 1. Find the largest number.
//
// 2. Find the second largest number.
//
// 3. Subtract 1 from both numbers.
//
// 4. Multiply them.
//
// 5. Return the maximum product.

// Algorithm:
//
// 1. Initialize two variables:
//      first = 0
//      second = 0
//
// 2. Traverse the array.
//
// 3. If the current number is greater
//    than or equal to first,
//      - Move first to second.
//      - Update first.
//
// 4. Otherwise, if the current number
//    is greater than second,
//      - Update second.
//
// 5. Return:
//      (first - 1) * (second - 1)

class Solution {
    public int maxProduct(int[] nums) {

        int first = 0;
        int second = 0;

        for (int num : nums) {

            if (num >= first) {
                second = first;
                first = num;
            } 
            else if (num > second) {
                second = num;
            }
        }

        return (first - 1) * (second - 1);
    }
}

// Interview Explanation:
//
// 1. I traversed the array only once.
//
// 2. I maintained the largest and
//    second largest elements.
//
// 3. Finally, I applied the formula:
//
//      (first - 1) * (second - 1)
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)