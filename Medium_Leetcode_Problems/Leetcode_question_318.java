// 💡 LOGIC
//
// We are given an array of words.
//
// We need to find two words that do NOT have any common characters.
//
// For every valid pair:
//
//     product = length(word1) * length(word2)
//
// We need to return the maximum product.
//
//
// ⭐ MAIN IDEA: BITMASK
//
// There are only 26 lowercase English letters.
//
// We can represent each character using one bit:
//
//     a -> bit 0
//     b -> bit 1
//     c -> bit 2
//     ...
//     z -> bit 25
//
// For every word, we create a bitmask representing
// all characters present in that word.
//
// If two words have no common characters:
//
//     (mask1 & mask2) == 0
//
// Then the two words are valid.
//
//
// 🔄 ALGORITHM
//
// 1. Create an integer array called masks.
//
// 2. For every word:
//      - Create mask = 0.
//      - Traverse every character.
//      - Find the character position:
//
//            int bit = word.charAt(j) - 'a';
//
//      - Set that bit:
//
//            mask = mask | (1 << bit);
//
//      - Store the mask.
//
// 3. Set answer = 0.
//
// 4. Compare every pair of words.
//
// 5. Check:
//
//        (masks[i] & masks[j]) == 0
//
//    If true, the two words have no common characters.
//
// 6. Calculate:
//
//        words[i].length() * words[j].length()
//
// 7. Update the maximum product.
//
// 8. Return answer.
//
//
// ⭐ KEY TRICK — BITMASK
//
// Example:
//
//     word1 = "abcw"
//     word2 = "xtfn"
//
// word1 contains:
//
//     a, b, c, w
//
// word2 contains:
//
//     x, t, f, n
//
// There are no common characters.
//
// Therefore:
//
//     mask1 & mask2 = 0
//
// So this is a valid pair.
//
// Lengths:
//
//     "abcw" = 4
//     "xtfn" = 4
//
// Product:
//
//     4 * 4 = 16
//
//
// 🧑‍💻 JAVA CODE

class Solution {

    public int maxProduct(String[] words) {

        // Store the bitmask of every word
        int[] masks = new int[words.length];

        // Create a bitmask for each word
        for (int i = 0; i < words.length; i++) {

            // Initially, no characters are present
            int mask = 0;

            // Process every character in the word
            for (int j = 0; j < words[i].length(); j++) {

                // Find the character position
                //
                // 'a' -> 0
                // 'b' -> 1
                // 'c' -> 2
                // ...
                // 'z' -> 25
                int bit = words[i].charAt(j) - 'a';

                // Set the corresponding bit
                mask = mask | (1 << bit);
            }

            // Store the mask of this word
            masks[i] = mask;
        }

        // Store the maximum product
        int answer = 0;

        // Compare every pair of words
        for (int i = 0; i < words.length; i++) {

            for (int j = i + 1; j < words.length; j++) {

                // Check if the two words have no common characters
                //
                // If AND is 0, there are no common characters.
                if ((masks[i] & masks[j]) == 0) {

                    // Calculate the product of their lengths
                    int product = words[i].length() * words[j].length();

                    // Update the maximum product
                    answer = Math.max(answer, product);
                }
            }
        }

        // Return the maximum product
        return answer;
    }
}


// 🧪 DRY RUN
//
// Input:
//
//     words = ["abcw", "xtfn"]
//
//
//
// Word 1:
//
//     "abcw"
//
// Characters:
//
//     a, b, c, w
//
//
// Word 2:
//
//     "xtfn"
//
// Characters:
//
//     x, t, f, n
//
//
// There is no common character.
//
// Therefore:
//
//     mask1 & mask2 = 0
//
//
// Lengths:
//
//     length("abcw") = 4
//     length("xtfn") = 4
//
//
// Product:
//
//     4 * 4 = 16
//
//
// Therefore:
//
//     answer = 16
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I use a bitmask to represent the characters present in each word.
// Since there are only 26 lowercase English letters, each character
// can be represented using one bit.
//
// For every pair of words, I perform a bitwise AND between their
// masks. If the result is zero, the two words do not share any
// common characters.
//
// Then I calculate the product of their lengths and keep track
// of the maximum product.
//
// Finally, I return the maximum product."
//
//
// ⭐ WHY BITMASK?
//
// A bitmask allows us to check whether two words share a character
// very efficiently.
//
// The condition:
//
//     (mask1 & mask2) == 0
//
// means that there is no common character between the two words.
//
//
// ⏱️ COMPLEXITY
//
// Let:
//
//     n = number of words
//     L = total number of characters in all words
//
// Creating all bitmasks:
//
//     O(L)
//
// Comparing every pair:
//
//     O(n²)
//
// Therefore:
//
//     Time Complexity = O(L + n²)
//
//     Space Complexity = O(n)
//
// The O(n) space is used to store the bitmask of every word.