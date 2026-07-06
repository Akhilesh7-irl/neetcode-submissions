class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        curLen = 0

        maxLen = 0
        
        for i in range(len(nums)):
            if curLen == 0:
                curLen = 1
                

            else:
                if nums[i] == nums[i-1]:
                    continue
                elif nums[i] == nums[i-1] + 1:
                    curLen += 1

                else:
                    
                    curLen = 1

            maxLen = max(curLen , maxLen)    

        return maxLen

            
            




        