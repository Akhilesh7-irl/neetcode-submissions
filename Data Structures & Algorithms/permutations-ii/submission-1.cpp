class Solution {
public:
    vector<vector<int>> res;
    
    void dfs(vector<int>& nums ,vector<bool>& used ,vector<int>& cur){
        if(cur.size() == nums.size()){
           res.push_back(cur);
           return;

        }
        

        for(int i= 0 ;i < nums.size(); i++){
            if(i > 0 && nums[i] == nums[i-1] && !used[i-1] ){
                continue;
            }


            if(!used[i]){
                cur.push_back(nums[i]);
                used[i] = true;
                dfs(nums , used , cur);
                cur.pop_back();
                used[i]= false;
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        vector<bool> used(nums.size() , false);
        
        vector<int> cur;
        dfs(nums , used , cur);
        return res;
        
    }
};