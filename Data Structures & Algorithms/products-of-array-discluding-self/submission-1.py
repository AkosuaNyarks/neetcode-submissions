class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results=[]
        for i in range(len(nums)):
            value=1
            for j in range(len(nums)):
                if i !=j:
                    value*=nums[j]
            results.append(value)
        return results
                    
        