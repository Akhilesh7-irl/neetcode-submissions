class Solution:
    def isValid(self, s: str) -> bool:
        tab = { "(" : ")",
                "[" : "]",
                "{" : "}"}
        if len(s)%2 != 0:
            return False
        map = [""]
        for c in s:
            if c in tab:
                map.append(c)
            
            else:
                try:    
                    if c == tab[map[-1]]:
                        map.pop()
                    else:
                        return False
                except KeyError:
                    return False
        map.remove("")


        return True if len(map) == 0 else False

        

        
            
                

                
            