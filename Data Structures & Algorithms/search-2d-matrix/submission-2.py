class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        innerleft=0
        innerright=len(matrix[0])-1
        while left<=right:
            mid=(left+right)//2
            if target>matrix[mid][-1]:
                left=mid+1
            elif target<matrix[mid][0]:
                right=mid-1

            else:
                break
        if not left<=right:
            return False
        while innerleft<=innerright:
            mid_value=(innerleft+innerright)//2
            if target>matrix[mid][mid_value]:
                innerleft=mid_value+1
            elif target<matrix[mid][mid_value]:
                innerright=mid_value-1
            else:
                return True
        return False

        