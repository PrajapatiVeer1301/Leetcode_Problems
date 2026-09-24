// 💡 Logic
//
// For each index i:
//
// 1. Find the sum of all digits of nums[i].
// 2. Check whether the digit sum is equal to index i.
// 3. If they are equal, return i.
//    Since we traverse from left to right, this is the smallest index.
// 4. If no index satisfies the condition, return -1.
//
//
// 🔄 Algorithm
//
// 1. Traverse the array from left to right.
// 2. Take nums[i] and calculate its digit sum.
// 3. Compare the digit sum with index i.
// 4. If digitSum == i, return i immediately.
// 5. If the loop finishes without finding a match, return -1.
//
//
// 🧑‍💻 Java Code

class Solution {
    public int smallestIndex(int[] nums) {

        // Traverse the array from left to right
        for (int i = 0; i < nums.length; i++) {

            // Store the current number
            int num = nums[i];

            // Variable to store the sum of digits
            int digitSum = 0;

            // Calculate the digit sum
            while (num > 0) {

                // Get the last digit and add it to digitSum
                digitSum += num % 10;

                // Remove the last digit
                num /= 10;
            }

            // Check whether digit sum is equal to index
            if (digitSum == i) {

                // Return immediately because this is
                // the smallest matching index
                return i;
            }
        }

        // No index satisfies the condition
        return -1;
    }
}


// 🧪 Dry Run
//
// Input:
// nums = [1, 10, 11]
//
//
// For i = 0:
//
// nums[0] = 1
// digit sum = 1
// index = 0
//
// 1 != 0
//
// So, continue to the next index.
//
//
// For i = 1:
//
// nums[1] = 10
// digit sum = 1 + 0 = 1
// index = 1
//
// 1 == 1
//
// Therefore, return 1.
//
// Output:
// 1
//
//
// ⭐ Key Trick
//
// Traverse the array from left to right.
//
// As soon as:
//
// digitSum == index
//
// return the index immediately.
//
// Because we check indexes in increasing order,
// the first matching index is always the smallest index.
//
//
// 🎯 Interview Explanation
//
// "I solve this problem by traversing the array from left to right.
// For every index, I calculate the sum of digits of the current number
// using modulo 10 to extract the last digit and integer division by 10
// to remove it.
//
// Then I compare the digit sum with the current index.
// If they are equal, I immediately return the index.
// Since the array is traversed from left to right, the first match
// is guaranteed to be the smallest valid index.
//
// If no index satisfies the condition, I return -1."
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n × d)
//
// n = number of elements in the array
// d = maximum number of digits in an element
//
// We visit every element and calculate its digit sum.
//
// Space Complexity: O(1)
//
// We only use a few variables such as i, num, and digitSum.