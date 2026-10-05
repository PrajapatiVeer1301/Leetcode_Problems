// 💡 LOGIC
//
// We need to find the third distinct maximum number.
//
// We maintain three variables:
//
// first  -> largest distinct number
// second -> second largest distinct number
// third  -> third largest distinct number
//
// Important:
// Duplicate values should be counted only once.
//
// Example:
//
// nums = [2, 2, 3, 1]
//
// Distinct values are:
//
// 3, 2, 1
//
// Therefore, the third maximum is 1.
//
//
// 🔄 ALGORITHM
//
// 1. Initialize first, second, and third.
//
// 2. Traverse every number in the array.
//
// 3. If the number is already equal to first,
//    second, or third, skip it.
//
// 4. If the number is greater than first:
//       Move second to third.
//       Move first to second.
//       Store number in first.
//
// 5. Else if the number is greater than second:
//       Move second to third.
//       Store number in second.
//
// 6. Else if the number is greater than third:
//       Store number in third.
//
// 7. After processing all numbers:
//       If third exists, return third.
//       Otherwise, return first.
//
//
// ⭐ KEY POINT
//
// "Distinct maximum" means duplicate values are counted only once.
//
// Example:
//
// [3, 3, 2, 1]
//
// Distinct values:
//
// [3, 2, 1]
//
// First maximum  = 3
// Second maximum = 2
// Third maximum  = 1
//
//
// 🧑‍💻 JAVA CODE

class Solution {
    public int thirdMax(int[] nums) {

        // Store the largest distinct value
        Long first = null;

        // Store the second largest distinct value
        Long second = null;

        // Store the third largest distinct value
        Long third = null;

        // Traverse every number in the array
        for (int num : nums) {

            // Convert int to long for safe comparison
            // with null values
            long value = num;

            // Ignore duplicate values
            if ((first != null && value == first) ||
                (second != null && value == second) ||
                (third != null && value == third)) {
                continue;
            }

            // If value is the largest number
            if (first == null || value > first) {

                // Shift the existing values
                third = second;
                second = first;
                first = value;
            }

            // If value is the second largest number
            else if (second == null || value > second) {

                // Move the old second maximum to third
                third = second;
                second = value;
            }

            // If value is the third largest number
            else if (third == null || value > third) {

                // Store value as the third maximum
                third = value;
            }
        }

        // If the third distinct maximum exists,
        // return it
        if (third != null) {
            return third.intValue();
        }

        // Otherwise, return the largest value
        return first.intValue();
    }
}


// 🧪 DRY RUN
//
// Example:
//
// nums = [2, 2, 3, 1]
//
// Initially:
//
// first = null
// second = null
// third = null
//
//
// Process 2:
//
// 2 is greater than first.
//
// first = 2
// second = null
// third = null
//
//
// Process next 2:
//
// 2 is already equal to first.
//
// Therefore, skip it.
//
//
// Process 3:
//
// 3 > first
//
// Shift the values:
//
// third = second
// second = first
// first = 3
//
// Now:
//
// first = 3
// second = 2
// third = null
//
//
// Process 1:
//
// 1 is not greater than first or second.
//
// Therefore:
//
// third = 1
//
//
// Final:
//
// first = 3
// second = 2
// third = 1
//
// Answer:
//
// 1
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I maintain three variables to store the first, second,
// and third distinct maximum values.
//
// While traversing the array, I ignore duplicate values.
// If the current number is larger than the first maximum,
// I shift the existing values down.
//
// Similarly, if it is larger than the second or third maximum,
// I update the appropriate variable.
//
// At the end, if a third distinct maximum exists, I return it.
// Otherwise, I return the first maximum.
//
// This allows me to solve the problem in one pass without
// sorting the array."
//
//
// ⏱️ COMPLEXITY
//
// Time Complexity: O(n)
//
// We traverse the array only once.
//
// Space Complexity: O(1)
//
// We use only three variables.
//
//
// ⭐ IMPORTANT EXAMPLE
//
// nums = [1, 2]
//
// Distinct values:
//
// [2, 1]
//
// There is no third distinct maximum.
//
// Therefore, we return the maximum:
//
// 2