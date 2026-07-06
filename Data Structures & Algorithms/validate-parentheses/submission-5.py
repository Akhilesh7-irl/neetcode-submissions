class Solution:
    def isValid(self, s: str) -> bool:
        tab = { "(" : ")",
                "[" : "]",
                "{" : "}"}

        map = [""]
        if len(s)%2 != 0:
            return False
        for n in s:
            try:
                if tab.get(n) not in s:
                    return False
            except TypeError:
                continue
        
        
        
        
        
        for n in s:
 
            if n in tab:
                map.append(n)
            else:
                if n == tab.get(map[-1]):
                    map.pop()
                else:
                    return False
        map.remove("")
        if len(map) == 0:
            return True
        else :
            return False
            
                

                
            