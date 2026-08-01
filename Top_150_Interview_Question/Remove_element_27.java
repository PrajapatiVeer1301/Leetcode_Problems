// Logic:
//
// 1. Initialize k = 0.
//
// 2. Traverse the array.
//
// 3. If the current element
//    is not equal to val,
//    copy it to index k.
//
// 4. Increment k.
//
// 5. Continue until the end
//    of the array.
//
// 6. Return k.

// Algorithm:
//
// 1. Set k = 0.
//
// 2. Traverse the array.
//
// 3. If nums[i] != val:
//
//      nums[k] = nums[i];
//
//      k++;
//
// 4. Return k.

class Solution {
    public int removeElement(int[] nums, int val) {

        int k = 0;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
}

// Dry Run:
//
// Input:
//
// nums = [3,2,2,3]
// val = 3
//
// k = 0
//
// ------------------------
//
// i = 0
// nums[0] = 3
//
// 3 == val
//
// Ignore
//
// k = 0
//
// ------------------------
//
// i = 1
// nums[1] = 2
//
// 2 != val
//
// nums[0] = 2
//
// k = 1
//
// Array:
// [2,2,2,3]
//
// ------------------------
//
// i = 2
// nums[2] = 2
//
// 2 != val
//
// nums[1] = 2
//
// k = 2
//
// Array:
// [2,2,2,3]
//
// ------------------------
//
// i = 3
// nums[3] = 3
//
// 3 == val
//
// Ignore
//
// ------------------------
//
// Final Array:
//
// [2,2,_,_]
//
// Return:
//
// k = 2

// Interview Explanation:
//
// 1. I used a pointer k to keep
//    track of the position where
//    the next valid element should
//    be placed.
//
// 2. I traversed the array once.
//
// 3. Whenever I found an element
//    different from val, I copied
//    it to index k and incremented k.
//
// 4. This modifies the array
//    in-place without using any
//    extra space.
//
// 5. Finally, I returned k,
//    which represents the number
//    of valid elements.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)
