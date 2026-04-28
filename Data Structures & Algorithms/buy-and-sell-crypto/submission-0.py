class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        sell_ptr = 1
        maxPrice = 0

        while sell_ptr < len(prices):
            if prices[buy_ptr] < prices[sell_ptr]:
                profit = prices[sell_ptr] - prices[buy_ptr]
                maxPrice = max(maxPrice, profit)
            else:
                buy_ptr = sell_ptr
            
            sell_ptr += 1
        
        return maxPrice
