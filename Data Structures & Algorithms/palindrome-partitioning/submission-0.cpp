class Solution {
public:
    vector<vector<string>> res;

    void backtrack(string s, int i, int l, vector<string> path) {
        if (i == s.size()) {
            res.push_back(path);
            return;
        }

        if (i + l > s.size()) {
            return;
        }

        string temp = s.substr(i, l);
        string rev = temp;
        reverse(rev.begin(), rev.end());

        if (temp == rev) {
            path.push_back(temp);
            backtrack(s, i + l, 1, path);
            path.pop_back();
        }

        backtrack(s, i, l + 1, path);
    }

    vector<vector<string>> partition(string s) {
        vector<string> path;
        backtrack(s, 0, 1, path);
        return res;
    }
};