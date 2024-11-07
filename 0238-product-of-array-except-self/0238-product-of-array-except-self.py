class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from itertools import accumulate 
        import operator
        result = nums.copy()
        prefix = list(accumulate(nums,operator.mul))
        suffix = list(accumulate(nums[::-1],operator.mul))[::-1]

        for i in range(len(nums)):
            if i==0:
                result[i] = suffix[i+1]
            elif i==len(nums)-1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1]*suffix[i+1]
        return result