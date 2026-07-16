class Solution {
public:
    vector<vector<string>> res;

    void backtrack(string s, int i,  vector<string> path) {
        if (i == s.size()) {
            res.push_back(path);
            return;
        }

        for( int k = i ;k < s.size() ; k++){
            string temp = s.substr(i , k-i+1);
            string og = temp;
            reverse(temp.begin() , temp.end());
            if(og == temp){
                path.push_back(temp);
                backtrack(s , k+1 ,path);
                path.pop_back();
            }
        }

        
    }

    vector<vector<string>> partition(string s) {
        vector<string> path;
        backtrack(s, 0, path);
        return res;
    }
    }
;