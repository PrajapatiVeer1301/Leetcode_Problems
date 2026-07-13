
// Logic:
//
// 1. Store the string "123456789".
//
// 2. Generate all possible sequential numbers
//    using substrings.
//
// 3. Convert each substring into an integer.
//
// 4. If the number is between low and high,
//    add it to the answer list.
//
// 5. Return the result.

// Algorithm:
//
// 1. Create the string "123456789".
//
// 2. Find the digit lengths of low and high.
//
// 3. Generate substrings of every valid length.
//
// 4. Convert each substring into an integer.
//
// 5. Check whether it lies in the range.
//
// 6. Add valid numbers to the result.
//
// 7. Return the result.

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {

        List<Integer> result = new ArrayList<>();

        String digits = "123456789";

        int lowLength = String.valueOf(low).length();
        int highLength = String.valueOf(high).length();

        for (int len = lowLength; len <= highLength; len++) {

            for (int i = 0; i <= 9 - len; i++) {

                int num = Integer.parseInt(digits.substring(i, i + len));

                if (num >= low && num <= high) {
                    result.add(num);
                }
            }
        }

        return result;
    }
}

// Interview Explanation:
//
// 1. I stored the digits "123456789" in a string.
//
// 2. Then I generated all possible sequential numbers
//    by taking substrings of different lengths.
//
// 3. I converted each substring into an integer.
//
// 4. If the generated number was within the given range,
//    I added it to the result.
//
// 5. Finally, I returned the list of sequential numbers.
//
// Time Complexity: O(1)
// Space Complexity: O(1)






