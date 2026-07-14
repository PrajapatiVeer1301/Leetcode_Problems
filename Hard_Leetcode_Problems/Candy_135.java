
// Logic:
//
// 1. Give every child one candy.
//
// 2. Traverse from left to right.
//    If a child's rating is higher than the left child,
//    give one more candy.
//
// 3. Traverse from right to left.
//    If a child's rating is higher than the right child,
//    update candies using Math.max().
//
// 4. Sum all candies.
//
// 5. Return the total.

// Algorithm:
//
// 1. Create a candies array.
//
// 2. Initialize every child with one candy.
//
// 3. Traverse from left to right.
//
// 4. Traverse from right to left.
//
// 5. Calculate the total candies.
//
// 6. Return the total.

class Solution {
    public int candy(int[] ratings) {

        int n = ratings.length;
        int[] candies = new int[n];

        // Give 1 candy to every child
        for (int i = 0; i < n; i++) {
            candies[i] = 1;
        }

        // Left to Right
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }

        // Right to Left
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }

        int total = 0;

        for (int candy : candies) {
            total += candy;
        }

        return total;
    }
}

// Interview Explanation:
//
// 1. I used a Greedy approach.
//
// 2. First, I gave one candy to every child.
//
// 3. Then I traversed from left to right
//    to satisfy the left neighbor condition.
//
// 4. After that, I traversed from right to left
//    to satisfy the right neighbor condition.
//
// 5. I used Math.max() to preserve the larger candy count.
//
// 6. Finally, I summed all candies and returned the answer.
//
// Time Complexity: O(n)
// Space Complexity: O(n)