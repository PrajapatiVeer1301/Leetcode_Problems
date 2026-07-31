// Logic:
//
// 1. Count the frequency of each character
//    in the given word.
//
// 2. Store all frequencies in an array.
//
// 3. Sort the frequencies in descending order.
//
// 4. The most frequent letters should require
//    the fewest key presses.
//
// 5. The first 8 most frequent letters
//    require 1 push.
//
// 6. The next 8 letters require 2 pushes.
//
// 7. The next 8 letters require 3 pushes.
//
// 8. The remaining letters require 4 pushes.
//
// 9. Multiply each character's frequency
//    by its required pushes and add
//    the result to the answer.
//
// 10. Return the minimum total pushes.

// Algorithm:
//
// 1. Create an integer array freq[26].
//
// 2. Count the frequency of each letter.
//
// 3. Sort the frequency array.
//
// 4. Traverse the sorted array
//    from highest frequency to lowest.
//
// 5. For each non-zero frequency:
//
//      pushes = (position / 8) + 1
//
//      answer += frequency * pushes
//
// 6. Return answer.

import java.util.*;

class Solution {
    public int minimumPushes(String word) {

        int[] freq = new int[26];

        // Count frequency
        for (char ch : word.toCharArray()) {
            freq[ch - 'a']++;
        }

        // Sort frequencies
        Arrays.sort(freq);

        int answer = 0;
        int position = 0;

        // Traverse from highest frequency
        for (int i = 25; i >= 0; i--) {

            if (freq[i] == 0)
                break;

            answer += freq[i] * ((position / 8) + 1);
            position++;
        }

        return answer;
    }
}

// Dry Run:
//
// Input:
//
// word = "aabbccddeeffgghhiiiiii"
//
// Frequency:
//
// a = 2
// b = 2
// c = 2
// d = 2
// e = 2
// f = 2
// g = 2
// h = 2
// i = 6
//
// After Sorting (Descending):
//
// 6, 2, 2, 2, 2, 2, 2, 2, 2
//
// answer = 0
// position = 0
//
// --------------------------------
//
// position = 0
// frequency = 6
// pushes = 1
// answer = 6 × 1 = 6
//
// --------------------------------
//
// position = 1
// frequency = 2
// pushes = 1
// answer = 6 + 2 = 8
//
// --------------------------------
//
// position = 2
// frequency = 2
// pushes = 1
// answer = 10
//
// --------------------------------
//
// position = 3
// frequency = 2
// pushes = 1
// answer = 12
//
// --------------------------------
//
// position = 4
// frequency = 2
// pushes = 1
// answer = 14
//
// --------------------------------
//
// position = 5
// frequency = 2
// pushes = 1
// answer = 16
//
// --------------------------------
//
// position = 6
// frequency = 2
// pushes = 1
// answer = 18
//
// --------------------------------
//
// position = 7
// frequency = 2
// pushes = 1
// answer = 20
//
// --------------------------------
//
// position = 8
// frequency = 2
// pushes = 2
// answer = 20 + (2 × 2)
// answer = 24
//
// --------------------------------
//
// Final Answer:
//
// 24

// Interview Explanation:
//
// 1. I counted the frequency of every
//    character in the string.
//
// 2. Since characters with higher
//    frequency should require fewer
//    key presses, I sorted the
//    frequencies in descending order.
//
// 3. I assigned:
//
//    First 8 frequencies  -> 1 push
//    Next 8 frequencies   -> 2 pushes
//    Next 8 frequencies   -> 3 pushes
//    Remaining frequencies-> 4 pushes
//
// 4. For each frequency, I multiplied
//    it by its assigned push count
//    and added it to the answer.
//
// 5. Finally, I returned the minimum
//    total number of pushes.
//
// Time Complexity: O(n + 26 log 26)
// ≈ O(n)
//
// Space Complexity: O(1)
