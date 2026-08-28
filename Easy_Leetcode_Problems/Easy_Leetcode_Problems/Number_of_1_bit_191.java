// 💡 Logic
//
// We check each bit of the number one by one.
//
// To get the last bit, use:
//
//     n & 1
//
// If the result is 1, then the current bit is a set bit.
//
// Then use:
//
//     n = n >> 1
//
// This shifts all bits one position to the right.
//
// We continue this process until n becomes 0.


// 🔄 Algorithm
//
// Step 1: Set count = 0.
//
// Step 2: While n > 0:
//
//         Check the last bit using:
//         n & 1
//
// Step 3: If (n & 1) == 1:
//
//         count++
//
// Step 4: Right shift n by one position:
//
//         n = n >> 1
//
// Step 5: Repeat until n becomes 0.
//
// Step 6: Return count.


// 🧪 Dry Run
//
// Input:
// n = 11
//
// Binary:
// 1011
//
// --------------------------------
//
// count = 0
//
// n = 1011
//
// n & 1 = 1
//
// Set bit found.
//
// count = 1
//
// Right shift:
//
// 1011 >> 1 = 0101
//
// --------------------------------
//
// n = 0101
//
// n & 1 = 1
//
// count = 2
//
// Right shift:
//
// 0101 >> 1 = 0010
//
// --------------------------------
//
// n = 0010
//
// n & 1 = 0
//
// count = 2
//
// Right shift:
//
// 0010 >> 1 = 0001
//
// --------------------------------
//
// n = 0001
//
// n & 1 = 1
//
// count = 3
//
// Right shift:
//
// 0001 >> 1 = 0000
//
// --------------------------------
//
// n = 0
//
// Stop.
//
// Final Answer:
// 3


// ☕ Java Code
//
// class Solution {
//     public int hammingWeight(int n) {
//
//         int count = 0;
//
//         while (n > 0) {
//
//             // Check the last bit
//             if ((n & 1) == 1) {
//                 count++;
//             }
//
//             // Right shift by 1 bit
//             n = n >> 1;
//         }
//
//         return count;
//     }
// }


// 🎯 Interview Explanation
//
// I use bit manipulation to count the set bits.
//
// The expression n & 1 checks whether the last bit
// of n is 1.
//
// If it is 1, I increment the count.
//
// Then I right shift n by one position using:
//
//     n = n >> 1
//
// This removes the last bit and allows me to check
// the next bit.
//
// I continue until n becomes 0.
//
// Time Complexity: O(log n)
//
// Space Complexity: O(1)


// ⭐ Key Trick
//
// n & 1
//     ↓
// Check the last bit
//
// Last bit = 1 → Set bit
// Last bit = 0 → Not a set bit
//
// n >> 1
//     ↓
// Move to the next bit


// 🚀 Follow-up: Brian Kernighan's Algorithm
//
// If the function is called many times,
// we can use:
//
//     n = n & (n - 1)
//
// This removes the lowest set bit directly.
//
// Therefore, the loop runs only once
// for every set bit.


// ⭐ Optimized Java Code
//
// class Solution {
//     public int hammingWeight(int n) {
//
//         int count = 0;
//
//         while (n != 0) {
//
//             n = n & (n - 1);
//             count++;
//         }
//
//         return count;
//     }
// }


// 🧪 Optimized Example
//
// n = 1011
//
// n - 1 = 1010
//
// 1011 & 1010 = 1010
// One set bit removed.
//
// 1010 & 1001 = 1000
// One more set bit removed.
//
// 1000 & 0111 = 0000
// One more set bit removed.
//
// Total set bits = 3.


// ⭐ Remember
//
// n & 1
//     ↓
// Check last bit
//
// n >> 1
//     ↓
// Move to next bit
//
// n & (n - 1)
//     ↓
// Remove lowest set bit