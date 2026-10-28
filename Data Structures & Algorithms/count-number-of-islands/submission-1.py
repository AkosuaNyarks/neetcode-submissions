class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])

        def dfs(grid,r,c):
            if r>=0 and r<row and c>=0 and c<col and grid[r][c]=="1":
                grid[r][c]="0"
                dfs(grid,r+1,c)
                dfs(grid,r-1,c)
                dfs(grid,r,c+1)
                dfs(grid,r,c-1)
            return

        numofIslands=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    numofIslands+=1
                    dfs(grid,r,c)
        return numofIslands

                    

       
        