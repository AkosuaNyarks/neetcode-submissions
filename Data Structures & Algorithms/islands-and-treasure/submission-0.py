class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visit.add((r,c))
                    queue.append((r,c))
                    
        distance=0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c]=distance
                check(grid,r+1,c,visit,queue)
                check(grid,r-1,c,visit,queue)
                check(grid,r,c+1,visit,queue)
                check(grid,r,c-1,visit,queue)
                                
            distance +=1
        
def check(grid,r,c,visit,queue):
    if  r<0 or r>=len(grid) or c<0 or c>=len(grid[0])or grid[r][c]==-1 or (r,c) in visit:
        return
    visit.add((r,c))
    queue.append((r,c))