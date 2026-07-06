class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [ [1,0] , [-1,0], [0,1] , [0,-1]]

        ROWS , COLS = len(grid) , len(grid[0])

        maxArea = 0
        Area = 0

        def dfs(r, c ):
            nonlocal Area , maxArea
            


            if(r<0 or c<0 or r>=ROWS  or c>=COLS or grid[r][c] == 0):
                maxArea = max(maxArea , Area)

                return

            grid[r][c] = 0
            Area += 1
            for dr , dc in directions:
                dfs(r+dr , c+dc)
                

            
        for r in range(ROWS):
            for c in range(COLS):
                Area = 0

                if grid[r][c] == 1:
                    dfs(r , c)           

            


        return maxArea

