class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tab = {"+" , "-" , "*" , "/"}


        res = 0
        if len(tokens) == 1:
            return int(tokens[0])
        map = []

        for n in tokens:
            if n in tab and map:
                b = map [len(map)-1]
                a =  map[len(map)-2]
                if n == "+":
                    res = a + b
                    map.pop()
                    map.pop()
                    map.append(res) 
                elif n == "-":
                    res =a - b
                    map.pop()
                    map.pop()
                    map.append(res)
                elif n == "*":
                    res = a * b
                    map.pop()
                    map.pop()
                    map.append(res)
                elif n == "/":
                    res = int(a / b)
                    map.pop()
                    map.pop()
                    map.append(res)                    
 
            else:
                map.append(int(n))
        
        
        
        return res


