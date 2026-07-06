class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for k in matrix:
            if target <= k[-1]:
                l, r = 0, len(k) - 1

                while l <= r:
                    
                    m = l + ((r - l) // 2)  

                    if k[m] > target:
                        r = m - 1
                    elif k[m] < target:
                        l = m + 1
                    else:
                        return True
                return False
            else:
                pass
        return False
        