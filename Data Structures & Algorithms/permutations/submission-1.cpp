class Solution {
public:
    vector<vector<int>> res;
    
    void dfs(vector<int>& nums ,vector<int> temp ,int num , vector<int> cur){
        if(cur.size() == nums.size()){
            res.push_back(cur);
            return;
        }
        erase(temp , num);

        for(int i= 0 ;i < temp.size(); i++){
            cur.push_back(temp[i]);
            
            dfs( nums ,temp , temp[i] , cur);
            cur.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> cur;
        vector<int> temp = nums;
        dfs(nums ,temp ,INT_MIN , cur);
        return res;
    }
};
