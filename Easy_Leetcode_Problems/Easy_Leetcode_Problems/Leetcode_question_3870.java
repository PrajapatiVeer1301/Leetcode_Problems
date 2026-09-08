// 💡 Simple Logic
//
// In this problem, n <= 10^5.
//
// Numbers from 1 to 999 contain 0 commas.
//
// Every number from 1000 to 99999 contains exactly 1 comma.
//
// The number 100000 contains 2 commas:
//
// 100000 -> 100,000 -> 1 comma
//
// IMPORTANT:
// Since n can be 100000, we need to handle it separately.
//
// If n < 1000:
//     Answer = 0
//
// If n >= 1000:
//     Numbers from 1000 to n each contribute 1 comma.
//
// Number of values from 1000 to n:
//
//     n - 1000 + 1
//
// which is:
//
//     n - 999
//
// If n >= 100000, add one extra comma because 100000 has 2 commas.


// 🔄 Algorithm
//
// 1. Count all numbers from 1000 to n.
//
//       answer = max(0, n - 999)
//
// 2. If n is at least 100000:
//
//       answer += 1
//
//    because 100000 contains 2 commas instead of 1.
//
// 3. Return answer.


// 🧪 Dry Run
//
// Example 1:
//
// n = 1002
//
// Numbers with commas:
//
// 1000 -> 1 comma
// 1001 -> 1 comma
// 1002 -> 1 comma
//
// Number of values:
//
// 1002 - 999 = 3
//
// n < 100000, so no extra comma.
//
// Answer = 3
//
//
// Example 2:
//
// n = 998
//
// All numbers have at most 3 digits.
//
// Therefore:
//
// Answer = 0
//
//
// Example 3:
//
// n = 100000
//
// Numbers from 1000 to 100000:
//
// 100000 - 999 = 99001
//
// This counts one comma for every number.
//
// But 100000 is:
//
// 100,000
//
// It has 2 commas, so we add one extra comma.
//
// Answer:
//
// 99001 + 1 = 99002


// 🎯 Interview Explanation
//
// "The key observation is that numbers from 1 to 999 do not contain
// any commas.
//
// Every number from 1000 to 99999 contains exactly one comma.
//
// Since n can be 100000, we also need to handle 100000 separately,
// because 100000 contains two commas.
//
// Therefore, I first count the numbers from 1000 to n using
// n - 999.
//
// If n is 100000, I add one extra comma.
//
// This gives an O(1) time and O(1) space solution."


// ⭐ Key Trick
//
// The important observation is:
//
// 1 to 999       -> 0 commas
// 1000 to 99999  -> 1 comma each
// 100000         -> 2 commas
//
// So we do not need to check every number individually.
//
// We can calculate the answer directly using a formula.


// ⏱️ Complexity
//
// Time Complexity: O(1)
//
// We perform only a few calculations.
//
// Space Complexity: O(1)
//
// We use only one variable for the answer.


// 🧑‍💻 Java Code

class Solution {
    public int countCommas(int n) {

        // Numbers from 1 to 999 have no commas.
        // Every number from 1000 to n has exactly one comma.
        //
        // Number of numbers from 1000 to n:
        // n - 1000 + 1 = n - 999

        return Math.max(0, n - 999);
    }
}