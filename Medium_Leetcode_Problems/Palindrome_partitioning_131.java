// Logic:
//
// 1. Use Backtracking.
//
// 2. Start from index 0.
//
// 3. Try every possible substring.
//
// 4. Check whether the substring
//    is a palindrome.
//
// 5. If it is a palindrome,
//    add it to current.
//
// 6. Recursively process the
//    remaining string.
//
// 7. Remove the last substring
//    after recursion.
//
// 8. When the complete string
//    is processed, store the
//    current partition.

// Algorithm:
//
// 1. Create an empty result list.
//
// 2. Call backtrack(s, 0).
//
// 3. For every index i:
//
//      part = s.substring(start, i + 1)
//
// 4. If part is palindrome:
//
//      Add part.
//
//      Call backtrack(i + 1).
//
//      Remove part.
//
// 5. If start == s.length():
//
//      Add current partition
//      to result.
//
// 6. Return result.

// Dry Run:
//
// Input:
//
// s = "aab"
//
// -------------------------
//
// start = 0
//
// Try "a"
//
// current = ["a"]
//
// -------------------------
//
// start = 1
//
// Try "a"
//
// current = ["a", "a"]
//
// -------------------------
//
// start = 2
//
// Try "b"
//
// current = ["a", "a", "b"]
//
// start = 3
//
// End of string.
//
// Store:
//
// ["a", "a", "b"]
//
// -------------------------
//
// Backtrack
//
// Remove "b"
//
// current = ["a", "a"]
//
// -------------------------
//
// Backtrack
//
// Remove second "a"
//
// current = ["a"]
//
// -------------------------
//
// Try "ab"
//
// "ab" is not palindrome.
//
// Ignore.
//
// -------------------------
//
// Backtrack
//
// Remove first "a"
//
// current = []
//
// -------------------------
//
// Try "aa"
//
// "aa" is palindrome.
//
// current = ["aa"]
//
// -------------------------
//
// start = 2
//
// Try "b"
//
// current = ["aa", "b"]
//
// End.
//
// Store:
//
// ["aa", "b"]
//
// -------------------------
//
// Final Answer:
//
// [
//   ["a", "a", "b"],
//   ["aa", "b"]
// ]

import java.util.*;

class Solution {

    public List<List<String>> partition(String s) {

        List<List<String>> result = new ArrayList<>();
        List<String> current = new ArrayList<>();

        backtrack(s, 0, current, result);

        return result;
    }

    private void backtrack(String s, int start,
                            List<String> current,
                            List<List<String>> result) {

        // Entire string is processed
        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Try every possible substring
        for (int i = start; i < s.length(); i++) {

            String part = s.substring(start, i + 1);

            // Check palindrome
            if (isPalindrome(part)) {

                current.add(part);

                // Process remaining string
                backtrack(s, i + 1, current, result);

                // Backtrack
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s) {

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {

            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}

// Interview Explanation:
//
// 1. I used Backtracking because
//    I need to generate all possible
//    palindrome partitions.
//
// 2. At every index, I tried every
//    possible substring.
//
// 3. I checked whether the substring
//    was a palindrome.
//
// 4. If it was a palindrome, I added
//    it to the current partition and
//    recursively processed the
//    remaining string.
//
// 5. After recursion, I removed the
//    substring to try another
//    possible partition.
//
// 6. When the complete string was
//    processed, I stored the
//    current partition.
//
// Time Complexity: O(n * 2^n)
//
// Space Complexity: O(n)