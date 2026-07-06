class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        res = 0
        nums = [-s for s in nums]
        heapq.heapify(nums)

        for a in range(k):
            res = heapq.heappop(nums)
                                                                                        
        return (-res)