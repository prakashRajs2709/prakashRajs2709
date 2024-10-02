class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binarySearch(arr, low, high, x):
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        numsset=set(nums)
        nums=list(numsset)
        nums.sort()
        left=0
        right=len(nums)-1
        result = binarySearch(nums, left, right, target)
        if result != -1:
            return True
        else:
            return False
        
                