class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[cnt]=nums[i]
                cnt+=1
        while cnt<len(nums):
            nums[cnt]=0
            cnt+=1
            
            
        