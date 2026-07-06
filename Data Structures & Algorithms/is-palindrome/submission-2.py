
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = list(s.lower())
        t = []
        for n in s:
            if n.isalpha() or n.isdigit():
                t.append(n)

        a = t[:]
        a.reverse()

        return t==a

        