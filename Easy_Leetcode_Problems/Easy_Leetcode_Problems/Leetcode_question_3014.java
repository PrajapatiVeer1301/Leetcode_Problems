// Logic:
//
// 1. There are 8 available keys (2 to 9).
//
// 2. The first 8 letters can each be
//    assigned to a different key,
//    so they require only 1 push.
//
// 3. The next 8 letters require
//    2 pushes each.
//
// 4. Every group of 8 letters
//    increases the required pushes by 1.
//
// 5. For each character at index i,
//    calculate:
//
//       (i / 8) + 1
//
// 6. Add the pushes for every character.
//
// 7. Return the total minimum pushes.

// Algorithm:
//
// 1. Initialize pushes = 0.
//
// 2. Traverse the string from
//    index 0 to word.length() - 1.
//
// 3. For each character,
//    calculate:
//
//       pushes += (i / 8) + 1
//
// 4. Continue until all characters
//    are processed.
//
// 5. Return pushes.

class Solution {
    public int minimumPushes(String word) {

        int pushes = 0;

        for (int i = 0; i < word.length(); i++) {
            pushes += (i / 8) + 1;
        }

        return pushes;
    }
}

// Interview Explanation:
//
// 1. Since there are only 8 keys,
//    the first 8 characters can be
//    assigned one per key, requiring
//    only 1 push each.
//
// 2. After filling all 8 keys,
//    the next 8 characters require
//    2 pushes each, and so on.
//
// 3. For each character at index i,
//    the required number of pushes is:
//
//       (i / 8) + 1
//
// 4. I traversed the string once,
//    calculated the pushes for each
//    character, and added them to
//    the final answer.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)

// Dry Run:
//
// Input:
//
// word = "xycdefghij"
//
// Length = 10
//
// pushes = 0
//
// ----------------------------------------
//
// i = 0
// Character = 'x'
// (0 / 8) + 1 = 1
// pushes = 0 + 1 = 1
//
// ----------------------------------------
//
// i = 1
// Character = 'y'
// (1 / 8) + 1 = 1
// pushes = 1 + 1 = 2
//
// ----------------------------------------
//
// i = 2
// Character = 'c'
// (2 / 8) + 1 = 1
// pushes = 2 + 1 = 3
//
// ----------------------------------------
//
// i = 3
// Character = 'd'
// (3 / 8) + 1 = 1
// pushes = 3 + 1 = 4
//
// ----------------------------------------
//
// i = 4
// Character = 'e'
// (4 / 8) + 1 = 1
// pushes = 4 + 1 = 5
//
// ----------------------------------------
//
// i = 5
// Character = 'f'
// (5 / 8) + 1 = 1
// pushes = 5 + 1 = 6
//
// ----------------------------------------
//
// i = 6
// Character = 'g'
// (6 / 8) + 1 = 1
// pushes = 6 + 1 = 7
//
// ----------------------------------------
//
// i = 7
// Character = 'h'
// (7 / 8) + 1 = 1
// pushes = 7 + 1 = 8
//
// ----------------------------------------
//
// i = 8
// Character = 'i'
// (8 / 8) + 1 = 2
// pushes = 8 + 2 = 10
//
// ----------------------------------------
//
// i = 9
// Character = 'j'
// (9 / 8) + 1 = 2
// pushes = 10 + 2 = 12
//
// ----------------------------------------
//
// Final Answer:
//
// pushes = 12
//
// Output:
//
// 12