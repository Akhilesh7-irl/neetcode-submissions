class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tab = []
        mainlist = []
        for i in range(len(strs)):
            y = sorted(strs[i])           
            sublist = []
            
            if y not in tab :
                sublist.append(strs[i])
                for  j in range(i+1,len(strs)):
                    x = sorted(strs[j])
                    tab.append(y)
                    
                    if x == y:
                        sublist.append(strs[j])

                mainlist.append(sublist)
                
            else:
                pass

             

        return mainlist     