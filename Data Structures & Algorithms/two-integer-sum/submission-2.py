class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Using Dictionaries
        prevDict={} 
        #Loop the list using the enumerate function
        for i,num in enumerate(nums):
            diff=target-num 
            # if the diff is in the dictonary,return the indexes of the 
            if diff in prevDict:
                return [prevDict[diff],i]
            #if not store the value in the dictionary
            prevDict[num]=i
        return
            