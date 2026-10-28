from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        
        
        frequent=[]
        for i in range(len(nums)+1):
            frequent.append([])
       

        for key,value in count.items():
            frequent[value].append(key)
        

        res=[]
        for i in range(len(frequent)-1,-1,-1):
            for n in frequent[i]:
                res.append(n)
                if len(res)==k:
                    return res
   





        