class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i ,a  in enumerate(nums):
            if a > 0:
                continue
            if i>0 and a == nums[i-1]:
                continue
            
            
            
            
            

            
            l = i+1
            r = len(nums)
            while l < r-1:
                y = nums[l] + nums[r-1]

                if y > -a:
                    r -= 1
                elif y < -a:
                    l += 1
                else:
                    
                    if sorted([nums[l],a,nums[r-1]]) not in res:
                        res.append(sorted([nums[l],a,nums[r-1]]))
                        l += 1
                        r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
                    

                
                
        return res
        
        

            
            
            