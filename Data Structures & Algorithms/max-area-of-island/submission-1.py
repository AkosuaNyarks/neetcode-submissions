class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    numOfIslands=self.dfs(grid,r,c)
                    max_island=max(max_island,numOfIslands)
                    print(max_island)
        return max_island
    
    def dfs(self,grid,r,c):
        island=1
        grid[r][c]=0
        lst=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        for r,c in lst:
            if r>=0 and r<len(grid) and c>=0 and c<len(grid[r]) and grid[r][c]==1:
                island+=self.dfs(grid,r,c)
        return island
        
