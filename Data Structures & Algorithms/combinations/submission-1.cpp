class Solution {
public:
    vector<vector<int>> res;
    
    
    void backtrack(int n , int k ,vector<int> cur, int start){
        if(cur.size() == k){
            res.push_back(cur);
            return;
        }
        for(int i = start ; i < n ; i++){
            cur.push_back(i+1);
            backtrack(n , k ,cur , i+1);
            cur.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        
        vector<int> cur;
        backtrack( n , k , cur , 0);
        
        return res;
        
    }
};