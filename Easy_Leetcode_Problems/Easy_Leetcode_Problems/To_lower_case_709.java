// 💡 LOGIC
//
// We need to convert every uppercase letter in the string
// into its corresponding lowercase letter.
//
// Example:
//
// "Hello"  →  "hello"
// "LOVELY" →  "lovely"
// "here"   →  "here"
//
// The string may also contain numbers and special characters.
// These characters should remain unchanged.
//
//
// ⭐ KEY TRICK — ASCII
//
// Uppercase letters are between:
//
// 'A' to 'Z'
//
// Lowercase letters are between:
//
// 'a' to 'z'
//
// The ASCII difference between an uppercase letter
// and its lowercase letter is 32.
//
// For example:
//
// 'A' = 65
// 'a' = 97
//
// 65 + 32 = 97
//
// Therefore, we can convert an uppercase character
// to lowercase using:
//
// (char)(ch + 32)
//
//
// 🔄 ALGORITHM
//
// 1. Create an empty StringBuilder.
//
// 2. Traverse every character of the string.
//
// 3. Check whether the character is an uppercase letter:
//
//       'A' <= ch && ch <= 'Z'
//
// 4. If it is uppercase:
//       Add 32 to its ASCII value.
//
// 5. If it is already lowercase or is another character:
//       Keep it unchanged.
//
// 6. Add the character to the StringBuilder.
//
// 7. Convert the StringBuilder to a String.
//
// 8. Return the final result.
//
//
// 🧑‍💻 JAVA CODE

class Solution {
    public String toLowerCase(String s) {

        // Store the final result
        StringBuilder result = new StringBuilder();

        // Traverse every character in the string
        for (char ch : s.toCharArray()) {

            // Check if the character is uppercase
            if (ch >= 'A' && ch <= 'Z') {

                // Convert uppercase character to lowercase
                // ASCII difference is 32
                ch = (char) (ch + 32);
            }

            // Add the character to the result
            result.append(ch);
        }

        // Return the converted string
        return result.toString();
    }
}


// 🧪 DRY RUN
//
// Example:
//
// s = "Hello"
//
// Process each character:
//
// H → h
// e → e
// l → l
// l → l
// o → o
//
// Final result:
//
// "hello"
//
// Answer = "hello"
//
//
// 🎯 INTERVIEW EXPLANATION
//
// "I traverse the string character by character.
// If the current character is an uppercase letter between
// A and Z, I convert it to lowercase using its ASCII value.
//
// The ASCII difference between an uppercase and lowercase
// letter is 32, so I add 32 to the uppercase character.
//
// If the character is already lowercase or is another
// printable character, I keep it unchanged.
//
// Finally, I return the resulting string."
//
//
// ⏱️ COMPLEXITY
//
// Time Complexity: O(n)
//
// Every character is processed exactly once.
//
// Space Complexity: O(n)
//
// We use a StringBuilder to store the resulting string.
//
// Here, n is the length of the input string.
//
//
// ⭐ IMPORTANT POINT
//
// We are not using the built-in toLowerCase() method.
// Instead, we manually convert uppercase letters using
// ASCII values.