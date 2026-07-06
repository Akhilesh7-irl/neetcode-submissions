class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False

            
        
        
        def dfs(n):
            nonlocal res
            if n >= len(nums)-1:
                res = True
                return

            for i in range(nums[n]):
                dfs(n+i+1)
                
            return

        dfs(0)
        return res








































































