class Solution {
public:
    vector<vector<int>> res;
    void dfs(vector<int>& candidates ,int target ,vector<int> cur  , int start){
        sort(candidates.begin() , candidates.end());
        if(target == 0){
            res.push_back(cur);
            return;
        }
        for(int i = start ; i < candidates.size() ; i++){
            if(i > start and candidates[i] == candidates[i-1]){
                continue;
            }
            int num = candidates[i];
            if(target - num >= 0){
                cur.push_back(num);
                dfs(candidates , target - num , cur , i+1);
                cur.pop_back();
            }
        }
            
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> cur;
        dfs(candidates , target , cur , 0);
        return res;
    }
};