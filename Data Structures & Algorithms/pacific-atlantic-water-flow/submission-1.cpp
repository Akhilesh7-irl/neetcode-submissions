class Solution {
public:
 
    bool a = false , p = false ;
    vector<vector<int>> res;
    
    

    void dfs(vector<vector<int>>& heights , int num ,int r , int c , int m , int n , vector<vector<bool>>& visit){
        if( r < 0 or r >= m or c < 0 or c >= n or visit[r][c] == true){
            return; 
        }
        if (heights[r][c] > num){
            return;
        }

        if (r == 0 || c == 0){
            p = true;
        }
        if(r == m-1 || c == n-1){
            a = true;
        }



        visit[r][c] = true;
        dfs(heights , heights[r][c] , r+1 , c , m , n ,visit);
        dfs(heights , heights[r][c] , r-1 , c , m , n, visit);
        dfs(heights ,heights[r][c] , r , c+1 , m , n, visit);
        dfs(heights ,heights[r][c] , r , c-1 , m , n, visit);
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        int m  = heights.size();
        int n = heights[0].size();
        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                a = false ; 
                p = false ;
                vector<vector<bool>> visit(m, vector<bool>(n, false));
                dfs(heights ,heights[i][j] , i , j , m , n , visit);

                if( a == true && p == true){
                    res.push_back({i , j});
                }

            }
        }

        return res;


    }
};
