class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new=sorted(set(nums))
        max_count=1
        count=1
        if not nums:
            return 0
        for i in range(len(new)):
            if new[i]-new[i-1]==1:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)
        return max_count