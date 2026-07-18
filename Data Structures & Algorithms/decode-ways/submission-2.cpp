class Solution {
public:
    int numDecodings(string s) {

        
        if (s[0] == '0') {
            return 0;
        }
        
        int a = (s.back() == '0') ? 0 : 1; 
        int b = 1;
        for( int i = s.size()-2 ; i >=0 ; i--){
            int temp = 0;

            if(s[i] != '0'){
                temp = a;

                int two = (s[i] - '0') *10 + (s[i + 1] - '0');
                if( two >= 10 && two <=26){
                    temp += b;
                }
            }

            b = a;
            a = temp;
        }
        return a;

        
    }
};
