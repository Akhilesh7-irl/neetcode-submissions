class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        
        hand.sort()
        i = 0
        size = 1
        temp = hand[0]
        hand.pop(0)
        while i < len(hand):
            
            if size == groupSize:
                i = 0
                temp = hand[0]
                hand.pop(0)
                size = 1
                continue
            if hand[i] == temp:
                i+=1
                continue
            if hand[i] == temp +1:
                size += 1
                
                temp = hand[i]
                hand.pop(i)
            else:
                return False

        if hand:
            return False

        else:
            return True

            

