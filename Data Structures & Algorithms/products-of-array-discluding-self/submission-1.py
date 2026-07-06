class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        for n in nums:
            
            
            mul  = mul*n
        nums1 = nums.copy()



        res = []
        for n in nums:
            if n != 0:
                x =  mul / n
                res.append(int(x))
            else:
                nums1.remove(0)
                mul2 = 1
                for n in nums1:
                    mul2 *= n
                nums1.append(0)
                

                res.append(int(mul2))

        
        return res