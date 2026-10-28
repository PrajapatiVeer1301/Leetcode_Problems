
class Solution {
    public String customSortString(String order, String s) {

        // ## LOGIC:
        // Count the frequency of every character in s.
        // Traverse order and add characters in the given order.
        // Finally, add characters that are not present in order.

        // Create an array to count lowercase English letters.
        int[] freq = new int[26];

        // Count the frequency of each character in s.
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            freq[ch - 'a']++;
        }

        // Store the final answer.
        StringBuilder result = new StringBuilder();

        // Add characters according to the custom order.
        for (int i = 0; i < order.length(); i++) {
            char ch = order.charAt(i);
            int index = ch - 'a';

            // Add the character according to its frequency.
            while (freq[index] > 0) {
                result.append(ch);
                freq[index]--;
            }
        }

        // Add characters that are not present in order.
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                result.append((char) ('a' + i));
                freq[i]--;
            }
        }

        // Return the final custom-sorted string.
        return result.toString();
    }
}

/*
## EXAMPLE:
Input:
order = "cba"
s = "abcd"

Output: "cbad"

## DRY RUN:
Step 1: Count characters in s.
a = 1, b = 1, c = 1, d = 1

Step 2: Traverse order = "cba".
c -> Add c
b -> Add b
a -> Add a

Result = "cba"

Step 3: Add remaining characters.
d -> Add d

Final output = "cbad"

## ALGORITHM:
1. Create a frequency array of size 26.
2. Count each character in s.
3. Traverse order and append each character
   according to its frequency.
4. Append all remaining characters.
5. Return the result.

## INTERVIEW EXPLANATION:
I use an integer array of size 26 to count the frequency
of each lowercase letter. Then I traverse order and append
each character as many times as it occurs in s. Finally,
I append any remaining characters and return the result.

## KEY TRICK:
ch - 'a' gives the array index of a lowercase letter.
For example, 'c' - 'a' = 2.

## TIME COMPLEXITY:
O(n + k + 26), where n is the length of s and k is
the length of order. Since 26 is constant, this is O(n + k).

## SPACE COMPLEXITY:
O(n + 26), including the output and frequency array.
This simplifies to O(n).
*/
