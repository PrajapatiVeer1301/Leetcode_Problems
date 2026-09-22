// 💡 Logic
//
// We need to convert a 32-bit integer into its hexadecimal representation
// without using Java's built-in hexadecimal conversion methods.
//
// Hexadecimal uses 16 characters:
//
// 0 1 2 3 4 5 6 7 8 9 a b c d e f
//
// ⭐ Key Trick
//
// Each hexadecimal digit represents exactly 4 binary bits.
//
// To get the last 4 bits, we use:
//
// num & 15
//
// because:
//
// 15 = 1111 in binary
//
// So, num & 15 extracts the last 4 bits.
//
// Then we move to the next 4 bits using:
//
// num >>> 4
//
// We use unsigned right shift (>>>) because the input can be negative.
//
// For a negative number, Java's int is already a 32-bit two's-complement
// value, so using >>> lets us process all 32 bits correctly.
//
//
// 🔄 Algorithm
//
// 1. If num == 0, return "0".
//
// 2. Create a string containing all hexadecimal characters:
//
//    hexChars = "0123456789abcdef"
//
// 3. While num is not 0:
//
//    - Get the last 4 bits using num & 15.
//    - Use that value as an index in hexChars.
//    - Add the corresponding character to the result.
//    - Unsigned shift num right by 4 bits.
//
// 4. The digits are generated from right to left,
//    so reverse the result.
//
// 5. Return the final hexadecimal string.
//
//
// 🧑‍💻 Java Code

class Solution {
    public String toHex(int num) {

        // If the number is 0, return "0"
        if (num == 0) {
            return "0";
        }

        // Store all hexadecimal digits
        String hexChars = "0123456789abcdef";

        // StringBuilder stores the result
        StringBuilder result = new StringBuilder();

        // Process 4 bits at a time
        while (num != 0) {

            // Get the last 4 bits
            int digit = num & 15;

            // Convert the digit into a hexadecimal character
            result.append(hexChars.charAt(digit));

            // Unsigned right shift by 4 bits
            num >>>= 4;
        }

        // Digits were generated from right to left,
        // so reverse the result
        return result.reverse().toString();
    }
}


// 🧪 Dry Run: num = 26
//
// Binary representation:
//
// 26 = 11010
//
// First iteration:
//
// 26 & 15 = 10
//
// Hexadecimal value of 10 = 'a'
//
// result = "a"
//
// Shift right by 4:
//
// 26 >>> 4 = 1
//
// Second iteration:
//
// 1 & 15 = 1
//
// Hexadecimal value of 1 = '1'
//
// result = "a1"
//
// The digits were generated from right to left.
//
// Reverse:
//
// "a1" → "1a"
//
// ✅ Answer = "1a"
//
//
// 🧪 Negative Example: num = -1
//
// In 32-bit two's complement:
//
// -1 = 11111111 11111111 11111111 11111111
//
// In hexadecimal:
//
// f f f f f f f f
//
// The loop extracts 'f' eight times:
//
// result = "ffffffff"
//
// After reversing:
//
// "ffffffff"
//
// ✅ Answer = "ffffffff"
//
//
// ⏱️ Complexity
//
// Time Complexity: O(1)
//
// A 32-bit integer has at most 8 hexadecimal digits,
// so the loop runs at most 8 times.
//
// Space Complexity: O(1)
//
// The result contains at most 8 characters.
//
//
// 🎯 Interview Explanation
//
// "I convert the integer to hexadecimal manually using bit operations.
// Since one hexadecimal digit represents 4 bits, I use num & 15
// to extract the last 4 bits and map them to a hexadecimal character.
// Then I use an unsigned right shift by 4 bits to process the next
// hexadecimal digit. For negative numbers, Java's int already uses
// 32-bit two's complement, and the unsigned shift allows me to process
// all 32 bits correctly. Finally, I reverse the result because the
// hexadecimal digits are generated from right to left."