// ----------- Logic ----------

// We use the array itself to detect duplicates.
//
// 1. Every number is in the range 1 to n.
//
// 2. For a number num, use:
//       index = num - 1
//
// 3. If nums[index] is positive, make it negative.
//    This means we have seen num for the first time.
//
// 4. If nums[index] is already negative,
//    num has appeared before, so it is a duplicate.
//
// 5. Add the duplicate number to the result list.

//------Algorithm------

// Step 1: Create an ArrayList<Integer> result.
//
// Step 2: Traverse the array.
//
// Step 3: Get the absolute value of nums[i]:
//
//       num = Math.abs(nums[i])
//
// Step 4: Calculate:
//
//       index = num - 1
//
// Step 5: If nums[index] < 0:
//
//       Add num to result.
//
// Step 6: Otherwise:
//
//       nums[index] = -nums[index]
//
// Step 7: Return result.

//---------Dry Run--------

// Input:
// nums = [4,3,2,7,8,2,3,1]
//
// --------------------------------
//
// num = 4
// index = 4 - 1 = 3
// nums[3] = 7 → make negative
//
// nums = [4,3,2,-7,8,2,3,1]
//
// --------------------------------
//
// num = 3
// index = 2
// nums[2] = 2 → make negative
//
// nums = [4,3,-2,-7,8,2,3,1]
//
// --------------------------------
//
// num = 2
// index = 1
// nums[1] = 3 → make negative
//
// nums = [4,-3,-2,-7,8,2,3,1]
//
// --------------------------------
//
// num = 7
// index = 6
// nums[6] = 3 → make negative
//
// nums = [4,-3,-2,-7,8,2,-3,1]
//
// --------------------------------
//
// num = 8
// index = 7
// nums[7] = 1 → make negative
//
// nums = [4,-3,-2,-7,8,2,-3,-1]
//
// --------------------------------
//
// num = 2
// index = 1
// nums[1] is already negative.
//
// Therefore 2 is a duplicate.
//
// result = [2]
//
// --------------------------------
//
// num = 3
// index = 2
// nums[2] is already negative.
//
// Therefore 3 is a duplicate.
//
// result = [2,3]
//
// --------------------------------
//
// Final Output:
//
// [2,3]


import java.util.*;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {

            int num = Math.abs(nums[i]);
            int index = num - 1;

            if (nums[index] < 0) {
                result.add(num);
            } else {
                nums[index] = -nums[index];
            }
        }

        return result;
    }
}

//--------- Interview Explanation -------

// I used the array itself to track whether a number
// has appeared before.
//
// Since every number is between 1 and n, I can use
// num - 1 as an index.
//
// When I encounter a number for the first time,
// I make nums[num - 1] negative.
//
// If I encounter the same number again, that position
// is already negative, so I know it is a duplicate.
//
// I add that number to the result list.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1) auxiliary space,
// excluding the output list.


// --------- ⭐ Key Trick ----------

// First time  → make nums[num - 1] negative
// Second time → already negative → duplicate