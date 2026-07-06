class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cursum = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                cursum = prices[r] - prices[l]
                maxprofit = max(maxprofit, cursum)
                r += 1
            else:
                l = r
                r += 1
        return maxprofit

            