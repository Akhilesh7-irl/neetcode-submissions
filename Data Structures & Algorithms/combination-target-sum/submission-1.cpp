class Solution {
public:
    vector<vector<int>> res;
    void dfs(vector<int>& nums ,int target ,vector<int> cur  , int start){
        
        if(target == 0){
            res.push_back(cur);
            return;
        }
        for(int i = start ; i < nums.size() ; i++){
            int num = nums[i];
            if(target - num >= 0){
                cur.push_back(num);
                dfs(nums , target - num , cur , i);
                cur.pop_back();
            }
        }
            
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> cur;
        dfs(nums , target , cur , 0);
        return res;
    }
};
