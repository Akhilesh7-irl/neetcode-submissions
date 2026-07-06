class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                break

        pivot = l
        k = pivot

        while True:
            if target == nums[pivot]:
                return pivot

            pivot += 1
            if pivot == len(nums):
                pivot = 0

            if pivot == k:
                return -1