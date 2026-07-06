class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cursum = 0
        l = 0
        r = 1

        for i in range(len(prices)):
            for j in range(i+1  , len(prices)):
                cursum = prices[j] - prices[i]
                maxprofit = max(maxprofit,cursum)
            
        return maxprofit
            