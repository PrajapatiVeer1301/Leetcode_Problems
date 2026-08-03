// Logic:
//
// 1. Since the array is sorted,
//    duplicate elements are adjacent.
//
// 2. The first element is always unique,
//    so initialize k = 1.
//
// 3. Traverse the array from index 1.
//
// 4. Compare the current element
//    with the last unique element.
//
// 5. If they are different,
//    store the current element
//    at index k.
//
// 6. Increment k.
//
// 7. Return k.

// Algorithm:
//
// 1. Initialize k = 1.
//
// 2. Traverse the array
//    from index 1.
//
// 3. If nums[i] != nums[k-1]:
//
//      nums[k] = nums[i];
//
//      k++;
//
// 4. Return k.

// Dry Run:
//
// Input:
//
// nums = [0,0,1,1,1,2,2,3,3,4]
//
// k = 1
//
// ----------------------------
//
// i = 1
//
// nums[1] = 0
//
// nums[k-1] = nums[0] = 0
//
// Same
//
// Ignore
//
// k = 1
//
// ----------------------------
//
// i = 2
//
// nums[2] = 1
//
// nums[k-1] = nums[0] = 0
//
// Different
//
// nums[1] = 1
//
// k = 2
//
// Array:
//
// [0,1,1,1,1,2,2,3,3,4]
//
// ----------------------------
//
// i = 3
//
// nums[3] = 1
//
// nums[k-1] = nums[1] = 1
//
// Same
//
// Ignore
//
// ----------------------------
//
// i = 5
//
// nums[5] = 2
//
// nums[k-1] = nums[1] = 1
//
// Different
//
// nums[2] = 2
//
// k = 3
//
// Array:
//
// [0,1,2,1,1,2,2,3,3,4]
//
// ----------------------------
//
// i = 7
//
// nums[7] = 3
//
// nums[k-1] = nums[2] = 2
//
// Different
//
// nums[3] = 3
//
// k = 4
//
// Array:
//
// [0,1,2,3,1,2,2,3,3,4]
//
// ----------------------------
//
// i = 9
//
// nums[9] = 4
//
// nums[k-1] = nums[3] = 3
//
// Different
//
// nums[4] = 4
//
// k = 5
//
// Final Array:
//
// [0,1,2,3,4,_,_,_,_,_]
//
// Return:
//
// k = 5

class Solution {
    public int removeDuplicates(int[] nums) {

        int k = 1;

        for (int i = 1; i < nums.length; i++) {

            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
}

// Interview Explanation:
//
// 1. Since the array is already sorted,
//    duplicate elements are placed
//    next to each other.
//
// 2. I used a pointer k to keep track
//    of the position where the next
//    unique element should be stored.
//
// 3. I traversed the array only once.
//
// 4. Whenever I found a new unique
//    element, I copied it to index k
//    and incremented k.
//
// 5. At the end, the first k elements
//    contain all unique elements,
//    and I returned k.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)