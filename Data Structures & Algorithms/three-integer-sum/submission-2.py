class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()                           
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ>0:
                    r-=1
                elif summ<0:
                    l+=1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
        ans=list(res)
        return ans
    