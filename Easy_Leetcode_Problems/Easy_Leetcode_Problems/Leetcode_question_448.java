// 💡 Logic
//
// We know that every number is in the range 1 to n.
//
// So, we can use the array indices to mark which numbers are present.
//
// For every number x:
//
// - Its corresponding index is x - 1.
// - Make nums[x - 1] negative.
// - After processing all elements, if nums[i] is still positive,
//   then number i + 1 is missing.
//
// The important point is to use Math.abs() because an element
// may already have been made negative.
//
//
// 🔄 Algorithm
//
// 1. Traverse the array.
//
// 2. For each element:
//       value = abs(nums[i])
//
// 3. Convert the value to an index:
//       index = value - 1
//
// 4. Make nums[index] negative.
//
// 5. Traverse the array again.
//
// 6. If nums[i] > 0:
//       i + 1 is missing.
//
// 7. Add all missing numbers to the result.
//
// 8. Return the result.
//
//
// 🧑‍💻 Java Code

import java.util.*;

class Solution {
    
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        // Mark the numbers that are present
        // by making the corresponding index negative
        for (int i = 0; i < nums.length; i++) {
            
            // Get the original value
            // Math.abs() is important because the value
            // may already have been made negative
            int value = Math.abs(nums[i]);
            
            // Convert the value into an array index
            int index = value - 1;
            
            // Mark this number as present
            nums[index] = -Math.abs(nums[index]);
        }
        
        // Store the missing numbers
        List<Integer> result = new ArrayList<>();
        
        // Check every index
        for (int i = 0; i < nums.length; i++) {
            
            // If the value is still positive,
            // the corresponding number is missing
            if (nums[i] > 0) {
                result.add(i + 1);
            }
        }
        
        // Return all missing numbers
        return result;
    }
}


// 🧪 Dry Run
//
// For:
//
// nums = [4,3,2,7,8,2,3,1]
//
// After marking the corresponding indices:
//
// [-4,-3,-2,-7,-8,2,-3,-1]
//
// Now check each index:
//
// index 0 → negative → 1 exists
// index 1 → negative → 2 exists
// index 2 → negative → 3 exists
// index 3 → negative → 4 exists
// index 4 → negative → 5 exists
// index 5 → positive → 6 is missing
// index 6 → negative → 7 exists
// index 7 → negative → 8 exists
//
// Therefore:
//
// [5, 6]
//
//
// 🎯 Interview Explanation
//
// "Since every number is in the range from 1 to n,
// I use the array indices to mark which numbers are present.
//
// For each value, I use value minus one as its corresponding
// index and make that element negative.
//
// After processing all elements, any index that still contains
// a positive value represents a missing number.
//
// This gives an O(n) solution with O(1) extra space,
// excluding the returned result."
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n)
// The array is traversed twice.
//
// Extra Space: O(1)
// No additional data structure is used.
//
// Result Space: O(k)
// Where k is the number of missing elements.