class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> map;
        int l = 0 , total = 0 , res = 0;

        for(int r = 0 ; r < fruits.size() ; r++){
            total++;
            map[fruits[r]]++;

            while(map.size() > 2){
                int k = fruits[l];
                map[k]--;
                total--;
                if(map[k] == 0){
                    map.erase(k);
                }
                l++;

            }
            res = max(res , total);
        }
        return res;
    }
};