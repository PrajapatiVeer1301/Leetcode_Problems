
// Logic:
//
// 1. Store all Roman numeral values in descending order.
//
// 2. Store their corresponding Roman symbols.
//
// 3. Start from the largest Roman value.
//
// 4. While the current value is less than or equal to the number:
//    - Append the corresponding Roman symbol.
//    - Subtract that value from the number.
//
// 5. Repeat until the number becomes 0.
//
// 6. Return the Roman numeral string.

// Algorithm:
//
// 1. Create an array of Roman values.
//
// 2. Create an array of Roman symbols.
//
// 3. Initialize an empty StringBuilder.
//
// 4. Traverse the Roman values array.
//
// 5. While num >= current Roman value:
//    - Append the corresponding Roman symbol.
//    - Subtract the Roman value from num.
//
// 6. Return the final Roman numeral string.


class Solution {
    public String intToRoman(int num) {

        int[] values = {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        };

        String[] symbols = {
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        };

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                result.append(symbols[i]);
                num -= values[i];
            }
        }

        return result.toString();
    }
}

// Interview Explanation:
//
// 1. I stored all Roman numeral values and symbols
//    in descending order.
//
// 2. Starting from the largest value,
//    I checked whether the number was greater than
//    or equal to the current Roman value.
//
// 3. If it was, I appended the corresponding Roman symbol
//    and subtracted that value from the number.
//
// 4. I repeated this process until the number became 0.
//
// 5. Finally, I returned the Roman numeral string.
//
// Time Complexity: O(1)
// Space Complexity: O(1)
