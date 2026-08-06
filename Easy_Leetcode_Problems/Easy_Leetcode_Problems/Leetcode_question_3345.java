// Logic:
//
// 1. Start checking from n.
//
// 2. Calculate the product
//    of all digits.
//
// 3. Check whether the
//    product is divisible by t.
//
// 4. If divisible,
//    return the number.
//
// 5. Otherwise,
//    increase n by 1.
//
// 6. Repeat until
//    the answer is found.

// Algorithm:
//
// 1. Start from n.
//
// 2. Find the product
//    of all digits.
//
// 3. If product % t == 0,
//    return n.
//
// 4. Otherwise,
//    increment n.
//
// 5. Repeat until
//    the answer is found.

// Dry Run:
//
// Input:
//
// n = 15
// t = 3
//
// --------------------
//
// Number = 15
//
// product = 1
//
// Last digit = 5
//
// product = 1 × 5 = 5
//
// num = 1
//
// Last digit = 1
//
// product = 5 × 1 = 5
//
// 5 % 3 = 2
//
// Not divisible
//
// n = 16
//
// --------------------
//
// Number = 16
//
// product = 1
//
// Last digit = 6
//
// product = 6
//
// num = 1
//
// Last digit = 1
//
// product = 6
//
// 6 % 3 = 0
//
// Divisible
//
// Return 16

class Solution {
    public int smallestNumber(int n, int t) {

        while (true) {

            int product = 1;
            int num = n;

            while (num > 0) {
                product *= (num % 10);
                num /= 10;
            }

            if (product % t == 0) {
                return n;
            }

            n++;
        }
    }
}
// Interview Explanation:
//
// 1. I started checking
//    from n.
//
// 2. For every number,
//    I calculated the
//    product of its digits.
//
// 3. If the product was
//    divisible by t,
//    I returned that number.
//
// 4. Otherwise,
//    I checked the next number.
//
// 5. Since n <= 100,
//    this brute-force solution
//    is efficient enough.
//
// Time Complexity: O(k × d)
//
// where:
// k = numbers checked
// d = digits in each number
//
// Space Complexity: O(1)