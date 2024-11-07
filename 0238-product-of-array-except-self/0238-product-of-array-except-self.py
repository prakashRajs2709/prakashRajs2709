class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from itertools import accumulate 
        import operator
        result  = []
        prefix = list(accumulate(nums,operator.mul))
        suffix = list(accumulate(nums[::-1],operator.mul))[::-1]

        for i in range(len(nums)):
            if i==0:
                result.append(suffix[i+1])
            elif i==len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])
        return result