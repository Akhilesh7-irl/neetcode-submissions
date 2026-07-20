class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<bool>> sur( m , vector<bool>(n , true));

        queue<pair<int , int>> q ;

        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if((i == 0 || j == 0) && board[i][j] == 'O'){
                    sur[i][j] = false;
                    q.push({i , j});
                }
                else if(( i == m-1 || j == n-1 )&& board[i][j] == 'O'){
                    sur[i][j] = false;
                    q.push({i , j});
                }
            }
        }
        vector<vector<int>> dirs = {{-1 , 0} ,{1,0} , {0 , -1} , {0 , 1}};

        while(!q.empty()){
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            
            for(int i = 0 ; i <4 ; i++){
                int r = row + dirs[i][0];
                int c = col + dirs[i][1];


                if(r < 0 || r >= m || c< 0 || c >= n || board[r][c] == 'X' || sur[r][c] == false){
                    continue;
                }
                sur[r][c] = false;
                
                q.push({r  , c});
            }


        }

        for(int i  = 0 ; i < m ; i++){
            for(int j = 0 ; j< n ; j++){
                if(board[i][j] == 'O' && sur[i][j] == true){
                    board[i][j] = 'X';
                }
            }
        }

        return;



    }
};
