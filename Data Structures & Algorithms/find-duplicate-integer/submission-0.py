class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tab = set()

        for n in nums:
            if n in tab:
                return n
            tab.add(n)

        return

         
        