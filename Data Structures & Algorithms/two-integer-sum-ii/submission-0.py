class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []
        
        while True:
            if numbers[left] + numbers[right] == target:
                res.append(left+1)
                res.append(right+1)
                break
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1

        return res     