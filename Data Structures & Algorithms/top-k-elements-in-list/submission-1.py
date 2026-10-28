from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary to count the occurences
        nums_dict=defaultdict(int)
        for num in nums:
            nums_dict[num]+=1
        #create a list of sublist(same number of elements in the list)
        res=[[] for i in range(len(nums)+1)]
        # loop through the dictionary for the keys and values and place them 
        #in corresponding list
        for keys,values in nums_dict.items():
            res[values].append(keys)
        #Create another empty list that keeps track of the most freq occuring number
        freq=[]
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                freq.append(n)
            #if the length of freq is equal to k then you retuen d
                if len(freq)==k:
                    return freq     

        



        