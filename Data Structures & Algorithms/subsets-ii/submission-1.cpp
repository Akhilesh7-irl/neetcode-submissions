class Solution {
public:
    vector<vector<int>> res;
    void dfs(vector<int>& nums , int start , vector<int>& path){
        res.push_back(path);

        for(int i = start ; i < nums.size() ; i++){
            if(i > start && nums[i] == nums[i-1]){
                continue;
            }
            path.push_back(nums[i]);
            dfs(nums ,i+1 , path);
            path.pop_back();
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        vector<int> path;
        dfs(nums , 0 , path);
        return res;
    }
};
