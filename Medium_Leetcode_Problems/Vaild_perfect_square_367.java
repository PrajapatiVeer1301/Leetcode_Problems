// ---------- 💡 Logic ----------

// 1. We need to check whether num is a perfect square.
//
// 2. A perfect square is a number that can be written as:
//
//       x * x = num
//
// 3. We use Binary Search to find x.
//
// 4. Set the search range:
//
//       left = 1
//       right = num
//
// 5. Find the middle value:
//
//       mid = left + (right - left) / 2
//
// 6. Calculate:
//
//       square = mid * mid
//
// 7. If square == num:
//       num is a perfect square.
//
// 8. If square < num:
//       Search on the right side.
//
//       left = mid + 1
//
// 9. If square > num:
//       Search on the left side.
//
//       right = mid - 1
//
// 10. If no value is found:
//        num is not a perfect square.


// ---------- 🔄 Algorithm ----------

// Step 1: Set:
//
//         left = 1
//         right = num
//
// Step 2: While left <= right:
//
//         mid = left + (right - left) / 2
//
// Step 3: Calculate:
//
//         square = (long) mid * mid
//
// Step 4: If square == num:
//
//         return true
//
// Step 5: If square < num:
//
//         left = mid + 1
//
// Step 6: Otherwise:
//
//         right = mid - 1
//
// Step 7: If the loop ends:
//
//         return false.


// ---------- 🧪 Dry Run ----------

// Input:
// num = 16
//
// --------------------------------
//
// left = 1
// right = 16
//
// --------------------------------
//
// mid = 1 + (16 - 1) / 2
//     = 8
//
// square = 8 * 8
//        = 64
//
// 64 > 16
//
// Therefore:
//
// right = 8 - 1
//       = 7
//
// --------------------------------
//
// left = 1
// right = 7
//
// mid = 1 + (7 - 1) / 2
//     = 4
//
// square = 4 * 4
//        = 16
//
// 16 == 16
//
// Therefore:
//
// return true
//
// --------------------------------
//
// Final Answer:
//
// true


// ---------- ☕ Java Code ----------

class Solution {
    public boolean isPerfectSquare(int num) {

        long left = 1;
        long right = num;

        while (left <= right) {

            long mid = left + (right - left) / 2;

            long square = mid * mid;

            if (square == num) {
                return true;
            }

            else if (square < num) {
                left = mid + 1;
            }

            else {
                right = mid - 1;
            }
        }

        return false;
    }
}


// ---------- 🎯 Interview Explanation ----------

// I use Binary Search to check whether there is an integer
// whose square is equal to num.
//
// I maintain a search range from 1 to num.
//
// In every iteration, I calculate the middle value
// and check mid * mid.
//
// If mid * mid equals num, then num is a perfect square.
//
// If mid * mid is smaller than num, I search on the right side.
//
// If mid * mid is greater than num, I search on the left side.
//
// If the binary search finishes without finding an exact square,
// I return false.
//
// I use long for mid and square to avoid integer overflow.
//
// Time Complexity: O(log n)
//
// Space Complexity: O(1)


// ---------- ⭐ Key Trick ----------

// Perfect Square:
//
//       mid * mid == num
//
// Example:
//
// num = 25
//
// 5 * 5 = 25
//
// Therefore → true
//
//
// Example:
//
// num = 26
//
// No integer x satisfies:
//
// x * x = 26
//
// Therefore → false


// ---------- 📌 Simple Understanding ----------

// Binary Search:
//
// If mid * mid is too small:
//
//       Move RIGHT
//
//       left = mid + 1
//
//
// If mid * mid is too large:
//
//       Move LEFT
//
//       right = mid - 1
//
//
// If mid * mid == num:
//
//       Perfect Square ✅
//
//
// Otherwise:
//
//       Not a Perfect Square ❌


// ---------- ⚠️ Important Java Point ----------

// Do not write:
//
//       int square = mid * mid;
//
// because mid * mid can overflow int.
//
// Instead use:
//
//       long square = mid * mid;
//
// Using long makes the multiplication safe.