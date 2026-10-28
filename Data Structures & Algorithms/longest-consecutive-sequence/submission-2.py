class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet=set(nums)
        longestSequence=0
        for num in newSet:
            if num-1 not in newSet:
                count=1
                while num+count in newSet:
                    count+=1
                longestSequence=max(longestSequence,count)
        return longestSequence