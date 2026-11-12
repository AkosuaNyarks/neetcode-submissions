class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows=len(heights)
        cols=len(heights[0])
        pacific_set=set()
        atlantic_set=set()

        def dfs (r,c,visited,prevHeight):
            if (r,c) in visited or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]< prevHeight:
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            


        for c in range(cols):
            dfs(0,c,pacific_set,heights[0][c])
            dfs(len(heights)-1,c,atlantic_set,heights[len(heights)-1][c])
        for r in range(rows):
            dfs(r,0,pacific_set,heights[r][0])
            dfs(r,len(heights[0])-1,atlantic_set,heights[r][len(heights[0])-1])
        return list(pacific_set & atlantic_set)



    