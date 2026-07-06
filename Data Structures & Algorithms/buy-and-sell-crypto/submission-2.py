class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minbuy = prices[0]

        for n in prices:
            maxp = max(maxp,n-minbuy)
            minbuy = min(minbuy,n)
        return maxp

            