from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
    
        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            queue.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append([r, c])
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1
            

        
        