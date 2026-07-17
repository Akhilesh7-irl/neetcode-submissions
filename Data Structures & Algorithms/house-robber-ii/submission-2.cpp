class Solution {
public:
    int rob(vector<int>& nums) {
        int a = 0 , b = 0;
        int c = 0 , d = 0;
        if (nums.size() == 1){
            return nums[0];
        }
        for(int i = 0 ; i < nums.size()-1 ; i++){
            int temp = max( b , a+nums[i]);
            a = b;
            b = temp;
        }
        
        for(int i = 1 ; i < nums.size() ; i++){
            int temp = max( d , c+nums[i]);
            c = d;
            d = temp;
        }
        return max(b , d);
    }
};
