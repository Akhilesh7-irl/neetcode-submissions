class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        maxcount = nums[0]

        for num in nums:
            if count < 0:
                count = 0

            count += num
            maxcount = max(maxcount , count)

        
        return maxcount