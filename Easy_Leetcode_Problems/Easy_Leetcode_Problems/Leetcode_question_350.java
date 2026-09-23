// 💡 Logic
//
// We will use a HashMap to store the frequency of elements.
//
// - Store the frequency of every element in nums1.
// - Then traverse through nums2.
// - If the current element is available in nums1,
//   add it to the result.
// - Decrease its frequency by 1.
// - When its frequency becomes 0, we cannot use that
//   element again.
//
//
// ⭐ Key Trick
//
// count.put(num, count.get(num) - 1);
//
// This decreases the available frequency of the element.
//
// It ensures that duplicate elements appear in the result
// only as many times as they appear in both arrays.
//
//
// 🔄 Algorithm
//
// 1. Create a HashMap to store the frequency of nums1.
//
// 2. Traverse nums1 and count every element.
//
// 3. Traverse nums2.
//
// 4. If num exists in the map and its frequency is greater than 0:
//    - Add num to the result.
//    - Decrease its frequency by 1.
//
// 5. Convert the result list into an array.
//
// 6. Return the result.
//
//
// 🧑‍💻 Java Code

import java.util.*;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        // Store the frequency of elements in nums1
        HashMap<Integer, Integer> count = new HashMap<>();

        // Count every element in nums1
        for (int num : nums1) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Store the intersection result
        List<Integer> result = new ArrayList<>();

        // Check every element in nums2
        for (int num : nums2) {

            // Check if the element is available
            if (count.containsKey(num) && count.get(num) > 0) {

                // Add the element to the result
                result.add(num);

                // Decrease its available frequency
                count.put(num, count.get(num) - 1);
            }
        }

        // Convert the result list into an int array
        int[] answer = new int[result.size()];

        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}


// 🧪 Dry Run
//
// nums1 = [1, 2, 2, 1]
// nums2 = [2, 2]
//
// Frequency of nums1:
//
// 1 → 2
// 2 → 2
//
//
// Process nums2:
//
// First 2:
//
// 2 is available
// result = [2]
// frequency of 2 = 1
//
//
// Second 2:
//
// 2 is available
// result = [2, 2]
// frequency of 2 = 0
//
//
// Final result:
//
// [2, 2]
//
//
// 🎯 Interview Explanation
//
// "I use a HashMap to store the frequency of every element
// in the first array. Then I traverse the second array.
// If the current element exists in the HashMap and its
// remaining frequency is greater than zero, I add it to
// the result and decrease its frequency.
//
// This ensures that every element appears in the result
// only as many times as it appears in both arrays."
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n + m)
//
// We traverse nums1 once and nums2 once.
//
// Space Complexity: O(n)
//
// The HashMap stores the frequencies of elements from nums1.
//
// n = length of nums1
// m = length of nums2
//
//
// 🔹 Follow-up
//
// 1. If both arrays are already sorted:
//
//    Use two pointers.
//    Compare the elements of both arrays and move the
//    appropriate pointer.
//
//    This uses O(1) extra space, excluding the result.
//
//
// 2. If nums1 is much smaller than nums2:
//
//    Build the frequency map using the smaller array
//    and scan the larger array.
//
//    This reduces the extra space required.
//
//
// 3. If nums2 is stored on disk and memory is limited:
//
//    Store the frequency information for the array that
//    fits in memory.
//
//    Then process nums2 in chunks instead of loading the
//    entire array into memory at once.