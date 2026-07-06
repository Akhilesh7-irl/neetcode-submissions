class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0){
            return false;
        }
        sort(hand.begin() , hand.end());
        int r = 0;
        int c = 1;
        int l = hand[0];
        hand.erase(hand.begin());

        while (r < hand.size()){
            if (c == groupSize){
                l = hand[0];
                hand.erase(hand.begin());
                
                c = 1;
                r = 0;
                continue;
            }
            if(hand[r] == l){
                r+=1;
                continue;
            }
            if ( hand[r] == l+1){
                c += 1;
                l = hand[r];
                hand.erase(hand.begin()+r);
            }
            else{
                return false;
            }

        }

        if(hand.size() > 0){
            return false;
        }
        return true;


    }
};
