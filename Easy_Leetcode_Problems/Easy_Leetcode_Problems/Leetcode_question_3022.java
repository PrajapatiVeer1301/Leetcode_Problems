// ---------- 💡 Logic ----------

// 1. Store the original number.
//
//       originalN = n
//
// 2. Initialize:
//
//       digitSum = 0
//       digitProduct = 1
//
// 3. Extract each digit using:
//
//       digit = n % 10
//
// 4. Add the digit to digitSum.
//
// 5. Multiply the digit with digitProduct.
//
// 6. Remove the last digit:
//
//       n = n / 10
//
// 7. Calculate:
//
//       divisor = digitSum + digitProduct
//
// 8. Check:
//
//       originalN % divisor == 0
//
// 9. If remainder is 0 → return true.
//    Otherwise → return false.


// ---------- 🔄 Algorithm ----------

// Step 1: Store the original value of n.
//
// Step 2: Set digitSum = 0.
//
// Step 3: Set digitProduct = 1.
//
// Step 4: While n > 0:
//
//         digit = n % 10
//
//         digitSum = digitSum + digit
//
//         digitProduct = digitProduct * digit
//
//         n = n / 10
//
// Step 5: Calculate:
//
//         divisor = digitSum + digitProduct
//
// Step 6: Check:
//
//         originalN % divisor == 0
//
// Step 7: Return true if divisible,
//         otherwise return false.


// ---------- 🧪 Dry Run ----------

// Input:
// n = 99
//
// --------------------------------
//
// originalN = 99
// digitSum = 0
// digitProduct = 1
//
// --------------------------------
//
// First digit:
//
// digit = 99 % 10
//       = 9
//
// digitSum = 0 + 9
//          = 9
//
// digitProduct = 1 * 9
//              = 9
//
// n = 99 / 10
//   = 9
//
// --------------------------------
//
// Second digit:
//
// digit = 9 % 10
//       = 9
//
// digitSum = 9 + 9
//          = 18
//
// digitProduct = 9 * 9
//              = 81
//
// n = 9 / 10
//   = 0
//
// --------------------------------
//
// divisor = digitSum + digitProduct
//
// divisor = 18 + 81
//         = 99
//
// --------------------------------
//
// Check:
//
// originalN % divisor
//
// 99 % 99 = 0
//
// Therefore:
//
// Output = true


class Solution {
    public boolean checkDivisibility(int n) {

        int originalN = n;

        int digitSum = 0;
        int digitProduct = 1;

        while (n > 0) {

            int digit = n % 10;

            digitSum += digit;
            digitProduct *= digit;

            n = n / 10;
        }

        int divisor = digitSum + digitProduct;

        return originalN % divisor == 0;
    }
}

// ---------- 🎯 Interview Explanation ----------

// I first store the original number because
// n is modified while extracting its digits.
//
// I calculate the digit sum and digit product
// by processing each digit one by one.
//
// I get the last digit using n % 10
// and remove the last digit using n / 10.
//
// Finally, I calculate the sum of digitSum
// and digitProduct.
//
// If the original number is divisible by this
// value, I return true; otherwise, I return false.
//
// Time Complexity: O(log n)
//
// Space Complexity: O(1)


// ---------- ⭐ Key Trick ----------

// digit = n % 10
// → Gets the last digit.
//
// n = n / 10
// → Removes the last digit.
//
// divisor = digitSum + digitProduct
//
// Answer:
//
// originalN % divisor == 0


// ---------- Example ----------

// n = 23
//
// digitSum = 2 + 3 = 5
//
// digitProduct = 2 * 3 = 6
//
// divisor = 5 + 6 = 11
//
// 23 % 11 = 1
//
// Therefore → false