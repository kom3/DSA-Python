# 121. Best Time to Buy and Sell Stock

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100




# Key insight: “best buy price so far”

# best_buy_price is the minimum price seen so far, including today.

# Conceptually: you want to buy at the lowest possible price up to this day, then sell today.

# If today’s price is lower than any previous day, you obviously wouldn’t have bought earlier — so you “pretend” to buy today.
# Even if best_buy_price is today’s price, the profit will be 0.

# Positive profit only happens if a future day’s price > buy price, which respects the “different future day” requirement.

# This is why this one-pass algorithm works perfectly for this problem.


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Returns the maximum profit from a single buy-sell transaction.

        Approach:
        - Track the minimum price seen so far (best day to buy).
        - For each day, calculate profit if we sell today.
        - Keep track of the maximum profit found.
        """

        # Initialize max profit to 0 (no transaction gives 0 profit)
        max_profit = 0

        # Initialize best buy price to infinity so first price becomes the new min
        best_buy_price = float('inf')

        # Loop through all prices (consider each day as a potential sell day)
        for price in prices:
            # Update the best buy price so far
            best_buy_price = min(best_buy_price, price)

            # Calculate current profit if we sell today
            curr_profit = price - best_buy_price

            # Update maximum profit
            max_profit = max(max_profit, curr_profit)

        return max_profit



# Single pass → O(n) time, O(1) space.