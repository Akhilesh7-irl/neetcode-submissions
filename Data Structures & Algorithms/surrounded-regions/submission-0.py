class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS , COLS = len(board) , len(board[0])


        def dfs(r,c , visit):
            if r>=ROWS  or c>= COLS or r < 0 or c < 0 or board[r][c] =="X" or (r,c) in visit:
                return

            board[r][c] = "#"
            visit.add((r,c))
            dfs(r+1 , c , visit)
            dfs(r-1 , c , visit)
            dfs( r, c+1 , visit)
            dfs(r , c-1 , visit)


        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                    dfs(r,c,set())


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"

        
        