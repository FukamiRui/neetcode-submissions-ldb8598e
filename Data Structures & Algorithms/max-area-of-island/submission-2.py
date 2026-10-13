class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        curr = 0
        visited = set()

        def dfs(r, c):
            nonlocal curr
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == 0 or (r, c) in visited):
                return 
            
            visited.add((r, c))
            curr += 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr = 0
                    dfs(r, c)
                    res = max(curr, res)
        return res
    
                    
        