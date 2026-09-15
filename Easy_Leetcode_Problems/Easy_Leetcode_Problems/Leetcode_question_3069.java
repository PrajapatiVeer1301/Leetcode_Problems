// 💡 Logic
//
// We will maintain two arrays:
//
// arr1
// arr2
//
// First, put the first element of nums into arr1.
//
// Then, put the second element of nums into arr2.
//
// After that, start from the third element, nums[2].
//
// For every remaining element:
//
// If the last element of arr1 is greater than
// the last element of arr2:
//
//     Add nums[i] to arr1
//
// Otherwise:
//
//     Add nums[i] to arr2
//
// Finally, concatenate arr1 and arr2.
//
//
// 🔄 Algorithm
//
// 1. Add nums[0] to arr1.
//
// 2. Add nums[1] to arr2.
//
// 3. Start a loop from index 2 to the end of nums.
//
// 4. Compare the last elements of arr1 and arr2.
//
// 5. If the last element of arr1 is greater than
//    the last element of arr2:
//       Add nums[i] to arr1.
//
// 6. Otherwise:
//       Add nums[i] to arr2.
//
// 7. After processing all elements, concatenate arr1 and arr2.
//
// 8. Return the final result.
//
//
// 🧪 Dry Run
//
// Example 1:
//
// nums = [2, 1, 3]
//
// Initially:
//
// arr1 = [2]
// arr2 = [1]
//
// Now process 3:
//
// Last element of arr1 = 2
// Last element of arr2 = 1
//
// Check:
//
// 2 > 1 → True
//
// Therefore, add 3 to arr1:
//
// arr1 = [2, 3]
// arr2 = [1]
//
// Finally:
//
// arr1 + arr2
// = [2, 3] + [1]
// = [2, 3, 1]
//
// Answer = [2, 3, 1]
//
//
// 🧪 Dry Run - Example 2
//
// nums = [5, 4, 3, 8]
//
// Initially:
//
// arr1 = [5]
// arr2 = [4]
//
//
// Process 3:
//
// Last element of arr1 = 5
// Last element of arr2 = 4
//
// 5 > 4 → True
//
// Add 3 to arr1:
//
// arr1 = [5, 3]
// arr2 = [4]
//
//
// Process 8:
//
// Last element of arr1 = 3
// Last element of arr2 = 4
//
// 3 > 4 → False
//
// Add 8 to arr2:
//
// arr1 = [5, 3]
// arr2 = [4, 8]
//
//
// Finally:
//
// [5, 3] + [4, 8]
// = [5, 3, 4, 8]
//
// Answer = [5, 3, 4, 8]
//
//
// 🎯 Interview Explanation
//
// "I will maintain two arrays, arr1 and arr2.
//
// I put the first element into arr1 and the second element
// into arr2.
//
// Then I iterate from the third element to the end.
//
// For each element, I compare the last elements of arr1 and arr2.
//
// If the last element of arr1 is greater, I add the current
// element to arr1.
//
// Otherwise, I add it to arr2.
//
// Finally, I concatenate arr1 and arr2 and return the result."
//
//
// ⭐ Key Trick
//
// The most important trick is to access the last element
// of an ArrayList using:
//
// arr1.get(arr1.size() - 1)
//
// Similarly:
//
// arr2.get(arr2.size() - 1)
//
// Then compare:
//
// if (arr1.get(arr1.size() - 1) > arr2.get(arr2.size() - 1))
//
// Finally, copy arr2 after arr1 to create the final result.
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// We process every element exactly once.
//
// Space Complexity: O(n)
//
// arr1 and arr2 together contain all n elements.
//
//
// 🧑‍💻 Java Code

import java.util.*;

class Solution {
    public int[] resultArray(int[] nums) {

        // Create the first array
        List<Integer> arr1 = new ArrayList<>();

        // Create the second array
        List<Integer> arr2 = new ArrayList<>();

        // Add the first element to arr1
        arr1.add(nums[0]);

        // Add the second element to arr2
        arr2.add(nums[1]);

        // Process all remaining elements
        for (int i = 2; i < nums.length; i++) {

            // Get the last element of arr1
            int lastArr1 = arr1.get(arr1.size() - 1);

            // Get the last element of arr2
            int lastArr2 = arr2.get(arr2.size() - 1);

            // Compare the last elements
            if (lastArr1 > lastArr2) {

                // Add the current element to arr1
                arr1.add(nums[i]);

            } else {

                // Add the current element to arr2
                arr2.add(nums[i]);
            }
        }

        // Create the final result array
        int[] result = new int[nums.length];

        // Copy all elements of arr1 into result
        int index = 0;

        for (int num : arr1) {
            result[index++] = num;
        }

        // Copy all elements of arr2 into result
        for (int num : arr2) {
            result[index++] = num;
        }

        // Return the final result
        return result;
    }
}