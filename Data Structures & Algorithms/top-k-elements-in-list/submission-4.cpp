class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int , int> m1;
        vector <vector<int>> freq(nums.size() +1);

        for(int n:nums){
            m1[n] += 1;
        }

        for(const auto& x:m1){
            freq[x.second].push_back(x.first);
        }
        vector<int> res;

        for(int i = freq.size() -1 ; i > 0 ; i--){
            for(int n: freq[i]){
                res.push_back(n);
                if(res.size() ==k){
                    return res;
                }
            }
        }
        return res;
    }
};
