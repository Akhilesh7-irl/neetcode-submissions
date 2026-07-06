class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                num = nums[i]
                
                if used[i] == False:
                    path.append(num)
                    used[i] = True

                    dfs(path)

                    path.pop()
                    used[i] = False
            
        dfs([])

        return res