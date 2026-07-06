class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        s = ""
        res = []


        def dfs(o , c ,s):
            if o == c == n :
                res.append(s)
                return
            if o < n:
                s += "("
                dfs(o+1 , c ,s)
                s = s[:-1]
            if c < o:
                s += ")"
                dfs(o , c+1 ,s)
                s = s[:-1]

            
        dfs(0,0 , s )

        return res
            


            