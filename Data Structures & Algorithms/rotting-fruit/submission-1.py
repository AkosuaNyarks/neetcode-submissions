class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        visited = set()
        queue=deque()
        fresh=0
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
                    visited.add((r,c))

        minute=0
        while queue and fresh>0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                fresh -=bfs(r+1,c,grid,visited,queue)
                fresh-=bfs(r-1,c,grid,visited,queue)
                fresh-=bfs(r,c-1,grid,visited,queue)
                fresh-=bfs(r,c+1,grid,visited,queue)
            minute+=1
        return minute if fresh==0 else -1

                    

def bfs(r,c,grid,visited,queue):
    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or grid[r][c]==2 or (r,c) in visited:
        return 0
    grid[r][c]=2
    visited.add((r,c))
    queue.append((r,c))
    return 1
    
        
        