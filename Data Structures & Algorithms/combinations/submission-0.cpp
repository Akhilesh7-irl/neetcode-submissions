class Solution {
public:
    vector<vector<int>> res;
    vector<int> arr;
    
    void backtrack(int n , int k ,vector<int> cur , vector<int> arr , int start){
        if(cur.size() == k){
            res.push_back(cur);
            return;
        }
        for(int i = start ; i < n ; i++){
            cur.push_back(arr[i]);
            backtrack(n , k ,cur , arr , i+1);
            cur.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        for(int i = 0 ; i < n ; i++){
            arr.push_back(i+1);
        }
        vector<int> cur;
        backtrack( n , k , cur , arr , 0);
        
        return res;
        
    }
};