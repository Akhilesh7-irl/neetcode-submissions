class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r =1 , max(piles)

        res = 0

        while l < r:
            m = (l + r) // 2

            totalh = 0

            for p in piles:
                totalh += math.ceil(p/m)
            
            if totalh <= h:
                r = m
            else:
                l = m+1
            
        return l

            
                
