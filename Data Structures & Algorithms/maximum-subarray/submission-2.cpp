class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int m = INT_MIN;
        int c = 0;
        for(int num : nums){
            c += num;
            if ( c < 0){
                c = 0;
                continue;
            }
            m = max( m , c);
        }
        return m == INT_MIN ? -1:m;
    }   
};
