class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tab = {}
        l = 0
        r = 0
        le = 0
        maxl = 0
        while r < len(s):
            tab[s[r]] = 1 + tab.get(s[r],0)
            if r-l+1 - max(tab.values()) <= k:
                r += 1
                le += 1
                maxl = max(maxl,le)
            else:
                tab.clear()
                l += 1
                r = l
                le = 0
        return maxl



            
        