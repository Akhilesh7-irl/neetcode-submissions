class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(target, path, start):
            if target == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                if target - num >= 0:
                    path.append(num)
                    dfs(target - num, path, i + 1)
                    path.pop()

        dfs(target, [], 0)
        return res