class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tab = {}
        l = 0
        r = 0
        le = 0
        maxl = 0
        while r < len(s):
            tab[s[r]] = 1 + tab.get(s[r],0)
            if (r-l+1) - max(tab.values()) <= k:
                maxl = max(maxl,r-l+1)
                r += 1
                
                
            else:
                tab[s[l]] -= 1
                l += 1
                r+=1
                
                
        return maxl



            
        