class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a set of empty list that are the size of the nums array:
        res=[] #[[][1][2][3,0][][]]
        for i in range(len(nums)+1):
            res.append([])

        #create a dictionary
        new_dict=defaultdict(int)#{7:2}
        for num in nums:
            new_dict[num]+=1

        # add the elements of the dictionary to res_list, by using their values as the list index to append
        for key,value in new_dict.items():
            res[value].append(key)
        
        # search the res list from behind, 
        #create a final list and add each element to the list and check if the length of the list is equal to k, 
        #return the list if it is
        final=[]
        for i in range(len(res)-1,-1,-1):
            for elem in res[i]:    
                final.append(elem)
                print(final)
                if len(final)==k:
                    return final




        



