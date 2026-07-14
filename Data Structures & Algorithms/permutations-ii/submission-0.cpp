class Solution {
public:
    vector<vector<int>> res;
    set<vector<int>> tab;
    
    void dfs(vector<int>& nums ,vector<bool>& used ,vector<int>& cur){
        if(cur.size() == nums.size()){
            if(tab.find(cur) == tab.end()){
                res.push_back(cur);
                tab.insert(cur);
            }
            return;
        }
        

        for(int i= 0 ;i < nums.size(); i++){
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
        vector<bool> used(nums.size() , false);
        
        vector<int> cur;
        dfs(nums , used , cur);
        return res;
        
    }
};