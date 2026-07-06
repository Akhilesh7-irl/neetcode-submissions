class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0


        def dfs(r,c):
            nonlocal count

            if r == m or c == n:
                return

            if (r,c) == (m-1 , n-1):
                count+=1
                return

            dfs(r+1 , c)
            dfs(r , c+1)

        
        dfs(0 , 0)

        return count

