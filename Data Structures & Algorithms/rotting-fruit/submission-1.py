class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])

        q = deque()

        visit = set()
        def RotFruit(r,c):
            if( min(r,c) < 0 or r == ROWS or c==COLS or grid[r][c] == 0 or (r,c) in visit):
                return

            grid[r][c] = 2

            visit.add((r,c))

            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])

                    visit.add((r,c))

        minute = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                RotFruit(r+1 , c)
                RotFruit(r-1, c)
                RotFruit(r, c+1)
                RotFruit(r, c-1)
            
            minute += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append([r,c])

        if q:
            return -1
        elif minute == 0:
            return 0

        else:
            return minute -1   

            

            

        
        

