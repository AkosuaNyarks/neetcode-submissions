class Solution:

    def midArray(self,matrix,target): 
        left =0
        right=len(matrix)-1
        while left <= right:
            mid=(left+right)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                return mid
            elif matrix[mid][0]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index=self.midArray(matrix,target)
        if index==-1:
            return False
        left=0
        right=len(matrix[index])-1
        while left<=right:
            mid=(left+right)//2
            if matrix[index][mid]==target:
                return True
            elif matrix[index][mid] < target:
                left=mid+1
            else:
                right=mid-1
        return False
        

            


