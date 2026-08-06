class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0
        
        for price in prices:
            buy1 = max(buy1, -price)               # best (most negative) cost for 1st buy
            sell1 = max(sell1, buy1 + price)        # best profit after 1st sell
            buy2 = max(buy2, sell1 - price)         # best net cost for 2nd buy (funded by 1st sell)
            sell2 = max(sell2, buy2 + price)        # best profit after 2nd sell
        
        return sell2