class Solution {
public:
    int res =0;
    void dfs(int r , int c , vector<vector<int>>& grid , int& area){


        if(r >= grid.size() || c >= grid[0].size() || r < 0 || c < 0||grid[r][c] == 0){
            return;
        }
        
        area += 1;
        grid[r][c] = 0;

        dfs(r+1 , c , grid , area);
        dfs(r-1 , c , grid , area);
        dfs(r , c+1 , grid , area);
        dfs(r , c-1 , grid , area);

        res = max(area , res);




    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        for(int i = 0 ; i < grid.size() ; i++){
            for(int j = 0 ; j < grid[0].size() ; j++){
                if (grid[i][j] == 1){
                    int area = 0;
                    dfs( i , j , grid , area);
                }
                
            }
        }

        return res;
        
    }
};
