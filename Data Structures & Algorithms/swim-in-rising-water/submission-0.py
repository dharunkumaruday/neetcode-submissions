import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))