class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0

        def backTracking(r, c):
            if (r < 0 or c < 0 or rows <= r or cols <= c or
                grid[r][c] == "0" or (r, c) in visited):
                return
            
            visited.add((r, c))

            backTracking(r + 1, c)
            backTracking(r - 1, c)
            backTracking(r, c + 1)
            backTracking(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    backTracking(r, c)
        return res        