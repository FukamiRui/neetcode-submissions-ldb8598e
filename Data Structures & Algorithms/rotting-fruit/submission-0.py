class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        res = []
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r, c))
        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((r, c))
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            
            if queue:
                time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time

       


