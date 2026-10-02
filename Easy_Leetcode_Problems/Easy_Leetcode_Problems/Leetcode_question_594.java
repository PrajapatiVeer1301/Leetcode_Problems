// 💡 LOGIC
//
// A harmonious array is an array where:
//
//     maximum value - minimum value == 1
//
// This means that if the minimum value is x,
// the maximum value must be x + 1.
//
// Therefore, for every number x, we check whether
// x + 1 exists in the array.
//
// If both x and x + 1 exist, we can use all their
// occurrences to form a harmonious subsequence.
//
// So the length will be:
//
//     count[x] + count[x + 1]
//
// We calculate this for every unique number and
// keep the maximum value.
//
//
// ⭐ KEY TRICK
//
// We use a HashMap to store the frequency of every number.
//
// Example:
//
// nums = [1, 3, 2, 2, 5, 2, 3, 7]
//
// Frequency:
//
// 1 -> 1
// 2 -> 3
// 3 -> 2
// 5 -> 1
// 7 -> 1
//
// Now check consecutive values:
//
// 1 and 2:
//     1 + 3 = 4
//
// 2 and 3:
//     3 + 2 = 5
//
// 3 and 4:
//     4 does not exist
//
// 5 and 6:
//     6 does not exist
//
// 7 and 8:
//     8 does not exist
//
// Maximum length = 5
//
//
// 🔄 ALGORITHM
//
// 1. Create a HashMap to store the frequency
//    of every number.
//
// 2. Traverse the nums array and count each number.
//
// 3. Traverse every unique number x in the HashMap.
//
// 4. Check whether x + 1 exists in the HashMap.
//
// 5. If x + 1 exists:
//
//       current = count[x] + count[x + 1]
//
// 6. Update the maximum answer.
//
// 7. After checking all numbers, return the maximum answer.
//
// 8. If no consecutive values exist, the answer
//    remains 0.
//
//
// 🧑‍💻 JAVA CODE

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findLHS(int[] nums) {

        // Store the frequency of every number
        Map<Integer, Integer> count = new HashMap<>();

        // Count the occurrences of each number
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Store the maximum harmonious subsequence length
        int answer = 0;

        // Check every unique number
        for (int num : count.keySet()) {

            // Check whether num + 1 exists
            if (count.containsKey(num + 1)) {

                // Use all occurrences of num and num + 1
                int current = count.get(num) + count.get(num + 1);

                // Update the maximum length
                answer = Math.max(answer, current);
            }
        }

        // Return the longest harmonious subsequence length
        return answer;
    }
}


// 🧪 DRY RUN
//
// Example:
//
// nums = [1, 3, 2, 2, 5, 2, 3, 7]
//
// Frequency Map:
//
// 1 -> 1
// 2 -> 3
// 3 -> 2
// 5 -> 1
// 7 -> 1
//
//
// Check 1:
//
// 1 + 1 = 2
//
// 2 exists.
//
// current = count[1] + count[2]
//         = 1 + 3
//         = 4
//
// answer = 4
//
//
// Check 2:
//
// 2 + 1 = 3
//
// 3 exists.
//
// current = count[2] + count[3]
//         = 3 + 2
//         = 5
//
// answer = 5
//
//
// Check 3:
//
// 3 + 1 = 4
//
// 4 does not exist.
//
//
// Check 5:
//
// 5 + 1 = 6
//
// 6 does not exist.
//
//
// Check 7:
//
// 7 + 1 = 8
//
// 8 does not exist.
//
//
// Therefore:
//
// answer = 5
//
// Final Output:
//
// 5
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I use a HashMap to store the frequency of every
// number in the array.
//
// For each unique number x, I check whether x + 1
// exists in the HashMap.
//
// If it exists, all occurrences of x and x + 1 can
// form a harmonious subsequence because their
// difference is exactly 1.
//
// So I calculate count[x] + count[x + 1] and keep
// track of the maximum value.
//
// Finally, I return the maximum length."
//
//
// ⏱️ COMPLEXITY
//
// Time Complexity: O(n) average
//
// We traverse the array once to build the frequency
// map and then traverse the unique elements.
//
// Space Complexity: O(n)
//
// In the worst case, all elements are unique, so the
// HashMap can contain n elements.
//
// Where:
//
// n = number of elements in the array
//
//
// ⭐ IMPORTANT POINT
//
// We do NOT need to actually construct the subsequence.
//
// Since a subsequence does not need to be contiguous,
// we can take all occurrences of x and x + 1.
//
// Therefore, their combined frequency gives the
// maximum possible length for that pair.