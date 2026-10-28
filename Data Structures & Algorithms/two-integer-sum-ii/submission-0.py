from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        results=[]
        resultsDict=defaultdict(int)
        for i in range(len(numbers)):
            value=target-numbers[i]
            if value in resultsDict:
                results.append(resultsDict[value]+1)
                results.append(i+1)
                return results
            else:
                resultsDict[numbers[i]]=i
                                
                                
                



        

        