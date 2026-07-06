class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        count = 0
        def dfs( n , stair):
            nonlocal count , res

            count += stair

            if count == n:
                res +=1
                count -= stair
                return
            
            if count > n:
                count -= stair
                return

            

            dfs(n , 1)
            dfs(n , 2)

            count -= stair
        dfs(n , 0)
        return res