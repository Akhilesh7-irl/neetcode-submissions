class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(target , path , start):
            if target == 0:
                res.append(path[:])
                return
        
            for i in range(start , len(nums)):
                num = nums[i]
                if target-num>=0:
                    path.append(num)
                    dfs(target - num , path , i)
                    path.pop()
                

        dfs(target , [] , 0)
        return res