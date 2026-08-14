// We use the Sliding Window technique.
//
// 1. Use two pointers: left and right.
//
// 2. Move right through the string.
//
// 3. Store the frequency of each character
//    in an integer array.
//
// 4. Each character can appear at most 2 times.
//
// 5. If a character appears more than 2 times,
//    move left forward until its frequency
//    becomes at most 2.
//
// 6. For every valid window, calculate:
//
//       right - left + 1
//
// 7. Store the maximum length.

// Step 1: Create an integer array of size 26
//         to store character frequencies.
//
// Step 2: Initialize:
//
//       left = 0
//       ans = 0
//
// Step 3: Traverse the string using right.
//
// Step 4: Increase frequency of s.charAt(right).
//
// Step 5: While the frequency of the current
//         character is greater than 2:
//
//       decrease frequency of s.charAt(left)
//       move left forward
//
// Step 6: Calculate current window length:
//
//       right - left + 1
//
// Step 7: Update ans.
//
// Step 8: Return ans.

// --------- Dry Run ------------

// Input:
// s = "aaaa"
//
// Initially:
//
// left = 0
// ans = 0
//
// --------------------------------
//
// right = 0
// window = "a"
// count[a] = 1
// length = 1
// ans = 1
//
// --------------------------------
//
// right = 1
// window = "aa"
// count[a] = 2
// length = 2
// ans = 2
//
// --------------------------------
//
// right = 2
// count[a] = 3 ❌
//
// 'a' occurs more than 2 times.
//
// Move left:
//
// remove s[0] = 'a'
// count[a] = 2
// left = 1
//
// window = "aa"
// length = 2
//
// ans = 2
//
// --------------------------------
//
// right = 3
// count[a] = 3 ❌
//
// Remove s[1]:
//
// count[a] = 2
// left = 2
//
// window = "aa"
// length = 2
//
// --------------------------------
//
// Final Answer:
//
// 2

class Solution {
    public int maximumLengthSubstring(String s) {

        int[] count = new int[26];

        int left = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);
            count[ch - 'a']++;

            while (count[ch - 'a'] > 2) {

                count[s.charAt(left) - 'a']--;
                left++;
            }

            ans = Math.max(ans, right - left + 1);
        }

        return ans;
    }
}

// Interview Explanation--

// I used the Sliding Window technique.
//
// I maintained two pointers, left and right,
// to represent the current substring.
//
// I used an integer array of size 26 to store
// the frequency of each lowercase character.
//
// I expanded the window using the right pointer.
//
// If any character appeared more than two times,
// I moved the left pointer forward and decreased
// its frequency until the window became valid.
//
// For every valid window, I calculated its length
// and updated the maximum length.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)
//
// The space is O(1) because there are only
// 26 lowercase English letters.

//  The key idea to remember for interview:

// Expand → Check frequency → Shrink → Update maximum
