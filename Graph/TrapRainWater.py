# Multi-source_BFS

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        ROWS, COLS = len(heightMap), len(heightMap[0])
        visited = set()
        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]
        # put all border cells to the heap, no water can be contained by them so makes sence to explore them first
        for row in range(ROWS):
            for col in range(COLS):
                if row in [0, ROWS-1] or col in [0, COLS-1]:
                    heapq.heappush(heap, (heightMap[row][col], row, col))
                    visited.add((row, col))
        
        #multi-source BFS
        maxheight = 0
        res = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            maxheight = max(maxheight, h)
            res += maxheight - h

            for d in DIRECTIONS:
                x, y = d
                new_r, new_c = r+x, c+y
                if (new_r, new_c) in visited:
                    continue
                if 0 <= new_r < ROWS and 0 <= new_c < COLS :
                    heapq.heappush(heap, (heightMap[new_r][new_c], new_r, new_c))
                    visited.add((new_r, new_c))


        return res
