class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max1 = 0;
        int l = 0;
        int r = heights.size() -1;

        while(l < r){
            int w = r-l;
            int h = min(heights[l] , heights[r]);
            max1 = max(max1 , w *h);
            if(heights[l] < heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return max1;
    }
};
