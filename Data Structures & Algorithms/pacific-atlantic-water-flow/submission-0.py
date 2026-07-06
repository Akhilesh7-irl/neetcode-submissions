class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS , COLS = len(heights) , len(heights[0])
        A , P = False , False
        res = []
        def dfs(num ,r , c):
            nonlocal A , P
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit:
                return

            if heights[r][c] > num:
                return



            if r == 0 or c == 0:
                P = True

            if r == ROWS-1 or c== COLS-1:
                A = True

            
                


            
            visit.add((r,c))
            dfs(heights[r][c] , r+1 , c)
            dfs(heights[r][c] , r-1 , c)
            dfs(heights[r][c] , r , c+1)
            dfs(heights[r][c] , r , c-1)


        for r in range(ROWS):
            for c in range(COLS):
                A = False

                P = False

                visit = set()
                dfs(heights[r][c] , r , c)

                if A == True and P == True:
                    res.append([r,c])

        
        return res
        