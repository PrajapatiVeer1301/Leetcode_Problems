// 💡 Logic
//
// We will use a HashSet to find duplicate elements.
//
// A HashSet does not store duplicate values.
//
// For example:
//
// nums = [1, 2, 3, 1]
//
// HashSet = {1, 2, 3}
//
// Original array length = 4
// HashSet length = 3
//
// Since both lengths are different, a duplicate exists.
//
// Therefore:
//
// nums.length != set.size()
//
// If this condition is true, the array contains a duplicate.
//
//
// 🔄 Algorithm
//
// 1. Create a HashSet.
//
// 2. Add every element of nums into the HashSet.
//
// 3. If an element is already present in the HashSet,
//    return true because a duplicate is found.
//
// 4. If all elements are added successfully,
//    return false because all elements are distinct.
//
//
// 🧑‍💻 Java Code

import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {

        // Create a HashSet to store unique elements
        HashSet<Integer> set = new HashSet<>();

        // Traverse through the array
        for (int num : nums) {

            // If the element already exists in the set,
            // a duplicate is found
            if (set.contains(num)) {
                return true;
            }

            // Add the element to the set
            set.add(num);
        }

        // No duplicate was found
        return false;
    }
}


// ⭐ Shortest Code

class Solution {
    public boolean containsDuplicate(int[] nums) {

        // Create a HashSet containing all elements
        Set<Integer> set = new HashSet<>();

        // Add all elements to the set
        for (int num : nums) {
            set.add(num);
        }

        // Different sizes mean duplicates exist
        return nums.length != set.size();
    }
}


// 🧪 Example
//
// nums = [1, 2, 3, 1]
//
// Initially:
//
// set = {}
//
// Add 1:
// set = {1}
//
// Add 2:
// set = {1, 2}
//
// Add 3:
// set = {1, 2, 3}
//
// Next element is 1.
//
// 1 is already present in the set.
//
// Therefore:
//
// return true
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// Space Complexity: O(n)
//
// n = number of elements in the array.
//
//
// 🎯 Interview Explanation
//
// "I use a HashSet to detect duplicate elements.
// HashSet stores only unique values.
// While traversing the array, I check whether the current
// element is already present in the HashSet.
// If it is present, I immediately return true.
// If I finish traversing the array without finding a duplicate,
// I return false."