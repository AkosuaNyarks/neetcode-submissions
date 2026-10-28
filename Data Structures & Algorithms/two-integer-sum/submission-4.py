class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results=[]
        resultDict=dict()
        for i in range(len(nums)):
            value=target-nums[i]
            if value in resultDict:
                results.append(i)
                results.append(resultDict[value])
                return sorted(results)
                
            else:
                resultDict[nums[i]]=i

                    
    
        