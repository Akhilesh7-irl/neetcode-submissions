class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tab = []
        l = 0
        r = 0
        le = 0
        maxl = 0
        while r < len(s):
            if s[r] not in tab:
                tab.append(s[r])
                r += 1
                le += 1
                maxl = max(maxl,le)

            else:
                tab.pop(0)
                l += 1
                
                le = len(tab)
        return maxl
                
        