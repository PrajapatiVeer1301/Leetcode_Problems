// Logic:
//
// 1. Sort both the greed array and cookie array.
//
// 2. Start from the smallest child and the smallest cookie.
//
// 3. If the cookie size is greater than or equal to
//    the child's greed factor,
//    satisfy the child.
//
// 4. Move to the next child.
//
// 5. Always move to the next cookie.
//
// 6. Return the total number of satisfied children.

// Algorithm:
//
// 1. Sort the greed array.
//
// 2. Sort the cookie array.
//
// 3. Initialize two pointers:
//    child = 0
//    cookie = 0
//
// 4. While both pointers are valid:
//
//    - If cookie >= greed,
//      satisfy the child.
//
//    - Move to the next cookie.
//
// 5. Return the number of satisfied children.



import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);

        int child = 0;
        int cookie = 0;

        while (child < g.length && cookie < s.length) {

            if (s[cookie] >= g[child]) {
                child++;
            }

            cookie++;
        }

        return child;
    }
}

// Interview Explanation:
//
// 1. I solved this problem using the Greedy approach.
//
// 2. First, I sorted both the greed array
//    and the cookie array.
//
// 3. Then I used two pointers.
//
// 4. If the current cookie could satisfy
//    the current child,
//    I assigned it to that child.
//
// 5. Otherwise, I tried the next larger cookie.
//
// 6. Finally, I returned the total number
//    of satisfied children.
//
// Time Complexity: O(n log n + m log m)
// Space Complexity: O(1)