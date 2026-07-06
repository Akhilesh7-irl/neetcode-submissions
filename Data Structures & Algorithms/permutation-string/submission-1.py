class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        tab = []
        while r < len(s2) and l<len(s2)-len(s1)+1:
            for i in range(len(s1)):
                tab.append(s2[r])
                r+=1
            if sorted(list(s1)) == sorted(tab) :
                return True
            else:
                tab.clear()
                l += 1
                r = l
        return False
            


        