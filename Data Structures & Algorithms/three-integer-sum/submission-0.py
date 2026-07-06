class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        for i in range(len(nums)):
            
            for j in range(i+1 , len(nums)):
                a = nums[:]
                x = nums[i]+nums[j]
                a.remove(nums[i])
                a.remove(nums[j])
                if -x in a:
                    mylist = [nums[i],nums[j],-x]
                    if sorted(mylist)  not in res:
                        res.append(sorted(mylist))
                    
                        

        
        return res