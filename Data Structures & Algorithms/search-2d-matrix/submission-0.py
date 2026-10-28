class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search the row
                       
        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] target = 10
        row=len(matrix)  #3
        column=len(matrix[0]) #4
        top=0
        bottom=len(matrix)-1
        
        while top <=bottom:
            mid_row=(top+bottom)//2 #1
            print
            if target > matrix[mid_row][-1]:
                top=mid_row+1
            elif target < matrix[mid_row][0]:
                bottom=mid_row -1
            else:
                break
        
        
        # then search the column
          
        #[10,11,12,13]
        left=0
        right=column-1
        while left<=right:
            mid_col=(left+right)//2
            if target==matrix[mid_row][mid_col]:
                return True

            
            elif target < matrix[mid_row][mid_col]:
                right=mid_col-1
            else:
                left=mid_col+1
        return False
    

        