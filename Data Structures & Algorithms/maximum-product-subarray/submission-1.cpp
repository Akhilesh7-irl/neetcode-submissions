class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int mn =1 , mx =1;

        for(auto num: nums){
            int tmp = mx * num;

            mx = max(num*mx , max(num*mn , num));
            mn = min(tmp , min(num*mn , num));
            res = max(res, mx);
        }
        return res;
    }
};
