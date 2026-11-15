class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        if len(prices) >= 2:
            
            index = []
            for i in range(len(prices)):
                for j in range(1+i, len(prices)):
                    r = prices[j] - prices[i]
                    if profit < r:
                        profit = r
                        index.clear()
                        index.append([i,j])
        return profit 
                    