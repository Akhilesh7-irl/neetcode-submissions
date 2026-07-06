class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tab = {}
        l = 0
        r = 0
        le = 0
        maxl = 0
        while r < len(s):
            if s[r] not in tab:
                tab[s[r]] = 1
                r += 1
                le += 1
                maxl = max(maxl,le)

            else:
                tab.pop(s[l])
                l += 1
                le = len(tab)
        return maxl
                
        