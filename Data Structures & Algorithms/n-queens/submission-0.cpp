class Solution {
public:
    unordered_set<int> col;
    unordered_set<int> rDiag;
    unordered_set<int> lDiag;
    vector<vector<string>> res;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n , string(n,'.'));

        backtrack(0, n , board);
        return res;
    }

private:
    void backtrack(int r , int n , vector<string>& board){
        if(r == n){
            res.push_back(board);
            return;
        }

        for(int c = 0; c < n; c++){
            if(col.count(c) || rDiag.count(r+c) || lDiag.count(r-c)){
                continue;
            }


            col.insert(c);
            rDiag.insert(r+c);
            lDiag.insert(r-c);

            board[r][c] = 'Q';

            backtrack(r+1, n , board);

            col.erase(c);
            rDiag.erase(r+c);
            lDiag.erase(r-c);
            board[r][c] = '.';
            
        }


    }



};
