class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        maxisland=0
        loop through each element in the grid
        countisland=0
        if 1: dfs on the one and convert all the 1s to 0s
        compare countisland to the maxisland using max func
        return maxisland
        """
        max_islands=[0]
        row=len(grid)
        col=len(grid[0])
        countislands=[0]
        def dfs(grid,r,c,countislands):
            if r>=0 and r<row and c>=0 and c<col and grid[r][c]==1:
                countislands[0]+=1
                grid[r][c]=0
                dfs(grid,r+1,c,countislands)
                dfs(grid,r-1,c,countislands)
                dfs(grid,r,c+1,countislands)
                dfs(grid,r,c-1,countislands)
            
            
            
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    dfs(grid,r,c,countislands)
                    max_islands[0]= max(countislands[0],max_islands[0])
                    countislands[0]=0
        
        return max_islands[0]