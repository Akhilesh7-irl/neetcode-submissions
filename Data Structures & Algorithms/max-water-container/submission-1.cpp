class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max1 = 0;
        int l = 0;
        int r = heights.size() -1;

        while(l < r){
            int m = 0;
            int a = heights[l];
            int b = heights[r];

            if (a > b) {
                m = (b*(r-l));
                r -= 1;
            }
            else if( b > a) {
                m = (a*(r-l));
                l += 1;

            }

            else{
                m =(a*(r-l));
                r-=1;
            }
            max1 = max( max1 , m );
        }
        return max1;
    }
};
