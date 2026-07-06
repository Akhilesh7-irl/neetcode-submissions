class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tab = {}
        for l in board:
            for i in l:
                if i == ".":
                    continue

                else:
                    if i in tab:
                        return False
                    else:
                        tab[i] = l.index(i)
            tab.clear()

        for i in range(9):
            for l in board:
                x  = l[i]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
            
            tab.clear()
        
        for i in range(3):
            for j in range(3):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(3):
            for j in range(3,6):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(3):
            for j in range(6,9):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()

        for i in range(3,6):
            for j in range(3):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(3,6):
            for j in range(3,6):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(3,6):
            for j in range(6,9):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(6,9):
            for j in range(3):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(6,9):
            for j in range(3,6):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()
        for i in range(6,9):
            for j in range(6,9):
                x = board[i][j]
                if x == ".":
                    continue

                else:
                    if x in tab:
                        return False
                    else:
                        tab[x] = i
        tab.clear()

        return True
                
        

            