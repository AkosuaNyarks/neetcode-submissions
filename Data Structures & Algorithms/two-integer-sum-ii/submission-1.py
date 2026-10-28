from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        results=[]
        left=0
        right=len(numbers)-1
        while left <right:
            value=numbers[left]+numbers[right]
            if value==target:
                results.append(left+1)
                results.append(right+1)
                return results
            elif value < target:
                left+=1
            else:
                right-=1                               
                                
                



        

        