// 💡 Logic
//
// We need to find the maximum length of a palindrome
// that can be created using the characters of the string.
//
// A palindrome needs characters in pairs.
//
// For example:
//
// "cc" → can be placed on the left and right sides.
//
// For every character, we can use the largest even part
// of its frequency.
//
// Example:
//
// frequency = 5
// usable part = 4
//
// frequency = 4
// usable part = 4
//
// frequency = 3
// usable part = 2
//
// If at least one character has an odd frequency,
// we can place ONE such character in the center.
//
// Therefore:
//
// - Add the largest even part of every frequency.
// - If any frequency is odd, add 1 for the center.
//
//
// 🔄 Algorithm
//
// 1. Create a frequency array of size 128.
//
// 2. Traverse the string and count the frequency
//    of every character.
//
// 3. For each frequency:
//    - Add the largest even part to answer.
//    - If the frequency is odd, remember that
//      we have an odd character.
//
// 4. If at least one odd frequency exists,
//    add 1 to answer.
//
// 5. Return answer.
//
//
// 🧑‍💻 Java Code

class Solution {
    public int longestPalindrome(String s) {

        // Store the frequency of each character
        int[] frequency = new int[128];

        // Count the frequency of every character
        for (char ch : s.toCharArray()) {
            frequency[ch]++;
        }

        // Store the length of the longest palindrome
        int answer = 0;

        // Check the frequency of every character
        for (int freq : frequency) {

            // Add the largest even part of the frequency
            answer += (freq / 2) * 2;
        }

        // Check if any character has an odd frequency
        for (int freq : frequency) {

            if (freq % 2 == 1) {

                // One odd character can be placed in the center
                answer++;

                // Only one odd character can be used in the center
                break;
            }
        }

        // Return the maximum palindrome length
        return answer;
    }
}


// 🧪 Dry Run
//
// s = "abccccdd"
//
// Frequency:
//
// a → 1
// b → 1
// c → 4
// d → 2
//
// Calculate the usable even parts:
//
// a → 0
// b → 0
// c → 4
// d → 2
//
// Total:
//
// 0 + 0 + 4 + 2 = 6
//
// There are odd frequencies:
//
// a → 1
// b → 1
//
// We can use ONE odd character in the center.
//
// Therefore:
//
// 6 + 1 = 7
//
// ✅ Answer = 7
//
//
// ⏱️ Complexity
//
// Time Complexity: O(n)
//
// We traverse the string once and then check
// the fixed-size frequency array.
//
// Space Complexity: O(1)
//
// The frequency array has a fixed size of 128.
//
//
// 🎯 Interview Explanation
//
// "I first count the frequency of every character using
// a frequency array. A palindrome requires matching pairs,
// so for each character I take the largest even part of
// its frequency. If there is at least one character with
// an odd frequency, I can place one occurrence of that
// character in the center. Therefore, I add all usable
// even frequencies and then add one if any odd frequency
// exists. This gives the maximum possible palindrome length."