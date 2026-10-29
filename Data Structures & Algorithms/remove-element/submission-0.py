class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for num in nums[:]:
            if val==num:
                print(num)
                k+=1
                nums.remove(val)

        return len(nums)
        