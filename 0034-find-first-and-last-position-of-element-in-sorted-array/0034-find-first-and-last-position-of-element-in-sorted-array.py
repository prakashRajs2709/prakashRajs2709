class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(arr,l,r,target,side):
            while l<=r:
                mid = (l+r)//2
                if arr[mid]<target:
                    l = mid+1
                elif arr[mid]>target:
                    r = mid-1
                else:
                    if side=='left' and mid>l and arr[mid]==arr[mid-1]:
                        r = mid
                    elif side=='right' and mid<r and arr[mid]==arr[mid+1]:
                        l = mid+1
                    else:
                        return mid
            return -1
        
        
        l = bs(nums,0,len(nums)-1,target,"left")
        r = bs(nums,0,len(nums)-1,target,"right")
        lst=[]
        lst.append(l)
        lst.append(r)
        return lst