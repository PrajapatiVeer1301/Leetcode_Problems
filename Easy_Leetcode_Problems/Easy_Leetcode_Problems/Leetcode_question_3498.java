// 💡 Logic
//
// We need to calculate the reverse degree of the string.
//
// Normal alphabet:
//
// a = 1, b = 2, c = 3, ..., z = 26
//
// Reversed alphabet:
//
// a = 26, b = 25, c = 24, ..., z = 1
//
// For every character, we find its reverse alphabet position.
//
// Formula:
//
// reversePosition = 'z' - ch + 1
//
// Then multiply it by the character's position in the string.
//
// The string position is 1-indexed, so:
//
// stringPosition = i + 1
//
// Finally, add all products to get the answer.
//
//
// 🔄 Algorithm
//
// 1. Initialize answer = 0.
//
// 2. Traverse every character in the string.
//
// 3. Find the character's reverse alphabet position.
//
// 4. Find its 1-based position using i + 1.
//
// 5. Multiply the reverse alphabet position by the string position.
//
// 6. Add the product to answer.
//
// 7. Return answer.
//
//
// 🧑‍💻 Java Code

class Solution {
    public int reverseDegree(String s) {

        // Store the total reverse degree
        int answer = 0;

        // Traverse through the string
        for (int i = 0; i < s.length(); i++) {

            // Get the current character
            char ch = s.charAt(i);

            // Find the reverse alphabet position
            int reversePosition = 'z' - ch + 1;

            // String position is 1-indexed
            int stringPosition = i + 1;

            // Multiply both positions and add to answer
            answer += reversePosition * stringPosition;
        }

        // Return the reverse degree
        return answer;
    }
}


// 🧪 Dry Run: "zaza"
//
// Character: z
// Reverse position = 1
// String position = 1
// Product = 1 × 1 = 1
//
// Character: a
// Reverse position = 26
// String position = 2
// Product = 26 × 2 = 52
//
// Character: z
// Reverse position = 1
// String position = 3
// Product = 1 × 3 = 3
//
// Character: a
// Reverse position = 26
// String position = 4
// Product = 26 × 4 = 104
//
// Total:
//
// 1 + 52 + 3 + 104 = 160
//
// ✅ Answer = 160
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// We visit every character exactly once.
//
// Space Complexity: O(1)
//
// We use only a few variables and no extra data structure.
//
// n = length of the string.
//
//
// 🎯 Interview Explanation
//
// "I traverse the string from left to right.
// For each character, I calculate its position in the
// reversed alphabet using 'z' - ch + 1.
// I multiply this value by the character's 1-based position
// in the string and add it to the total answer.
// After processing all characters, I return the total reverse degree."