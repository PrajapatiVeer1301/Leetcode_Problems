// Logic:
//
// 1. Convert the number into a String.
//
// 2. Traverse every pair of digits.
//
// 3. Convert characters into integers.
//
// 4. Find the product of every pair.
//
// 5. Store the maximum product.
//
// 6. Return the maximum product.

// Algorithm:
//
// 1. Convert n to String.
//
// 2. Initialize maxProduct = 0.
//
// 3. Use two nested loops.
//
// 4. Convert each character to digit.
//
// 5. Calculate:
//      product = digit1 * digit2
//
// 6. Update maxProduct.
//
// 7. Return maxProduct.

class Solution {
    public int maxProduct(int n) {

        String num = String.valueOf(n);

        int maxProduct = 0;

        for (int i = 0; i < num.length(); i++) {
            for (int j = i + 1; j < num.length(); j++) {

                int digit1 = num.charAt(i) - '0';
                int digit2 = num.charAt(j) - '0';

                maxProduct = Math.max(maxProduct, digit1 * digit2);
            }
        }

        return maxProduct;
    }
}


// ⭐ Optimized Java Solution (Without Converting to String)

class Solution {
    public int maxProduct(int n) {

        int first = 0;
        int second = 0;

        while (n > 0) {
            int digit = n % 10;

            if (digit >= first) {
                second = first;
                first = digit;
            } else if (digit > second) {
                second = digit;
            }

            n /= 10;
        }

        return first * second;
    }
}

// Interview Explanation:
//
// 1. I converted the number into a String.
//
// 2. I used two nested loops to
//    compare every pair of digits.
//
// 3. I converted each character
//    into an integer.
//
// 4. I calculated the product of
//    every pair and kept the
//    maximum product.
//
// 5. Finally, I returned the
//    maximum product.
//
// Time Complexity: O(d²)
// Space Complexity: O(d)
//
// where d = number of digits in n.

