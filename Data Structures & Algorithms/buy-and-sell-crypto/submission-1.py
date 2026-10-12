class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # check to see if left+1 is less than left, if it is, assign left to left+1
        # ELSE calculate the profit, only update it if profit is greater.
        profit, left = 0, prices[0]

        for price in prices:
            temp_profit = price - left
            if price < left:
                left = price
            elif temp_profit > profit:
                    profit = temp_profit

        return profit
            
