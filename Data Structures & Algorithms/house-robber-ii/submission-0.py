class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0] , self.cal(nums[1:]), self.cal(nums[:-1]))



    def cal(self,nums):
        rob1 , rob2 = 0,0

        for num in nums:
            temp = max(rob1+num , rob2)
            rob1 = rob2
            rob2 = temp

        return rob2