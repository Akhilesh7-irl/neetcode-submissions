class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        l = 0
        r = len(heights)-1

        while l<r:
            a = heights[l]
            b = heights[r]

            if a > b:
                res.append(b*(r-l))
                r -= 1
            elif b>a:
                res.append(a*(r-l))
                l+=1
            else:
                res.append(a*(r-l))
                r -= 1
        
        return max(res)
        