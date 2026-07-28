// Logic:
//
// 1. Count the frequency of each character.
//
// 2. Traverse characters from 'a' to 'z'.
//
// 3. Add half of each character's
//    frequency to the first half.
//
// 4. If a character has an odd frequency,
//    store it as the middle character.
//
// 5. Reverse the first half to
//    create the second half.
//
// 6. Return:
//
//    firstHalf + middle + secondHalf

// Algorithm:
//
// 1. Create an array of size 26
//    to count character frequencies.
//
// 2. Count the frequency of each character.
//
// 3. Build the first half of the palindrome.
//
// 4. Find the middle character
//    (if frequency is odd).
//
// 5. Reverse the first half.
//
// 6. Concatenate:
//
//      firstHalf + middle + secondHalf
//
// 7. Return the palindrome.

class Solution {
    public String smallestPalindrome(String s) {

        int[] count = new int[26];

        // Count frequency of each character
        for (char ch : s.toCharArray()) {
            count[ch - 'a']++;
        }

        StringBuilder firstHalf = new StringBuilder();
        String middle = "";

        // Build the first half and find the middle character
        for (int i = 0; i < 26; i++) {

            for (int j = 0; j < count[i] / 2; j++) {
                firstHalf.append((char) ('a' + i));
            }

            if (count[i] % 2 == 1) {
                middle = String.valueOf((char) ('a' + i));
            }
        }

        String secondHalf = new StringBuilder(firstHalf).reverse().toString();

        return firstHalf.toString() + middle + secondHalf;
    }
}

// Interview Explanation:
//
// 1. I counted the frequency of each character
//    using an array of size 26.
//
// 2. I built the first half of the palindrome
//    by taking half of each character's frequency
//    in alphabetical order.
//
// 3. If a character had an odd frequency,
//    I placed one occurrence in the middle.
//
// 4. I reversed the first half to create
//    the second half.
//
// 5. This guarantees the lexicographically
//    smallest palindromic permutation.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)
//
// (The frequency array size is fixed at 26.)