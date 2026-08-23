// ---------- 💡 Logic ----------

// 1. Initialize profit = 0.
//
// 2. Traverse the array starting from index 1.
//
// 3. If:
//
//       prices[i] > prices[i - 1]
//
//    Then:
//
//       profit += prices[i] - prices[i - 1]
//
// 4. If the price decreases, do not add anything
//    to the profit.
//
// 5. Finally, return profit.


// ---------- 🔄 Algorithm ----------

// Step 1: Set profit = 0.
//
// Step 2: Start the loop from index 1.
//
// Step 3: Compare the current price with
//         the previous price.
//
// Step 4: If current price > previous price:
//
//         profit = profit + (current price - previous price)
//
// Step 5: Otherwise, do nothing.
//
// Step 6: Continue until the end of the array.
//
// Step 7: Return profit.


// ---------- 🧪 Dry Run ----------

// Input:
// prices = [7, 1, 5, 3, 6, 4]
//
// --------------------------------
//
// profit = 0
//
// --------------------------------
//
// i = 1
//
// prices[1] = 1
// prices[0] = 7
//
// 1 > 7 → False
//
// profit = 0
//
// --------------------------------
//
// i = 2
//
// prices[2] = 5
// prices[1] = 1
//
// 5 > 1 → True
//
// profit = 0 + (5 - 1)
//        = 4
//
// --------------------------------
//
// i = 3
//
// prices[3] = 3
// prices[2] = 5
//
// 3 > 5 → False
//
// profit = 4
//
// --------------------------------
//
// i = 4
//
// prices[4] = 6
// prices[3] = 3
//
// 6 > 3 → True
//
// profit = 4 + (6 - 3)
//        = 7
//
// --------------------------------
//
// i = 5
//
// prices[5] = 4
// prices[4] = 6
//
// 4 > 6 → False
//
// profit = 7
//
// --------------------------------
//
// Final Answer:
//
// 7


// ---------- ☕ Java Code ----------

class Solution {
    public int maxProfit(int[] prices) {

        int profit = 0;

        for (int i = 1; i < prices.length; i++) {

            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }

        return profit;
    }
}


// ---------- 🎯 Interview Explanation ----------

// I use a greedy approach.
//
// I compare every day's price with the previous day's price.
//
// Whenever the current price is greater than the previous
// price, I add the difference to the total profit.
//
// This works because we are allowed to buy and sell
// the stock multiple times.
//
// For example:
//
// [1, 5, 3, 6]
//
// Profit = (5 - 1) + (6 - 3)
//        = 4 + 3
//        = 7
//
// Therefore, we capture every profitable price increase.
//
// Time Complexity: O(n)
//
// Space Complexity: O(1)


// ---------- ⭐ Key Trick ----------

// Only add positive differences:
//
// if (prices[i] > prices[i - 1]) {
//     profit += prices[i] - prices[i - 1];
// }
//
// Increasing:
//
// 1 → 5
// profit = +4
//
// 3 → 6
// profit = +3
//
// Total = 7
//
// Decreasing:
//
// 7 → 1
// profit = +0
//
// 6 → 4
// profit = +0


// ---------- 📌 Easy Formula ----------

// Maximum Profit =
// Sum of all positive consecutive differences
//
// For:
//
// [7, 1, 5, 3, 6, 4]
//
// (5 - 1) + (6 - 3)
//
// = 4 + 3
//
// = 7