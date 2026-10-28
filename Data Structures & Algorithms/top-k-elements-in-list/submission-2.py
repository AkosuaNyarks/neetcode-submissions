class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort
        # final list
        final=[]
        # create an empty list that is the length of the array
        res=[]
        for i in range(len(nums)+1):
            res.append([])
        print(res)
        #create a dictionary the has the value and its frequency as key-value pairs
        new_dict=defaultdict(int)
        for i in range(len(nums)):
            new_dict[nums[i]]+=1
        print(new_dict)
        #get the keys and values for elements in the dictionary
        for key, value in new_dict.items():
            res[value].append(key)
        print(res)
        #iterating th res list from bottom up
        for i in range(len(res)-1,0,-1):
            for digit in res[i]:
                final.append(digit)
                if len(final)==k:
                    return final
        