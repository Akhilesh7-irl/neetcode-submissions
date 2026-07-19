class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int res = 0;

        int fresh = 0;
        queue<pair<int , int>> q ; 


        for(int i = 0 ; i  < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if (grid[i][j] == 2){
                    q.push({i , j});
                    
                }
                else if(grid[i][j] == 1){
                    fresh ++;
                }
            }
        }
        vector<pair<int , int>> dirs = {{-1 , 0} ,{1,0} , {0 , -1} , {0 , 1}};

        while(!q.empty()){
            int sz = q.size();
            
            bool spread = false;
            for(int i = 0 ; i <sz; i++){
                auto [row , col] = q.front();
                q.pop();


                for(auto [dr , dc] : dirs){
                    int r = row + dr;
                    int c = col + dc;
                    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1)
                        continue;

                    grid[r][c] = 2;
                    fresh--;
                    spread = true;
                    q.push({r, c});
                }
            }
            if(spread) res++;

            
            
        }

        return fresh == 0 ? res:-1;
    }
};
