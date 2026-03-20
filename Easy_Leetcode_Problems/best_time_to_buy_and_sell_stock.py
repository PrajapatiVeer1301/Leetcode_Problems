
# Approach:
# 1. Keep track of the minimum stock price seen so far.
# 2. For each day, calculate the profit if we sell on that day.
# 3. Compare this profit with the maximum profit found so far.
# 4. Update the maximum profit whenever a larger profit is found.
# 5. If no profit is possible, return 0.

# Logic:
# - min_price stores the lowest price till the current day.
# - max_profit stores the highest profit possible.
# - For every price:
#     profit = current_price - min_price
# - If current_price is smaller than min_price, update min_price.
# - If profit is greater than max_profit, update max_profit.
# - At the end, return max_profit.

# Complexity:
# Time Complexity: O(n) where n is the number of days (length of prices array).
# Space Complexity: O(1) since we are using only a constant amount of space.    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach:
        # Keep track of the minimum price seen so far.
        # For each price, calculate the profit if sold on that day.
        # Update the maximum profit whenever a better profit is found.

        # Initialize minimum price as the first day's price
        min_price = prices[0]

        # Initialize maximum profit as 0
        max_profit = 0

        # Traverse through the price list
        for price in prices:
            # Update minimum price if current price is smaller
            if price < min_price:
                min_price = price

            # Calculate profit if sold today
            profit = price - min_price

            # Update maximum profit if current profit is higher
            if profit > max_profit:
                max_profit = profit

        # Return the final maximum profit
        return max_profit