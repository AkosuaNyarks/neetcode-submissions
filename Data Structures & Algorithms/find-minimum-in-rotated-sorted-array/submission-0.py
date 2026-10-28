class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
                     
        # [3,4,5,6,1,2]
                
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
        return nums[left]

        