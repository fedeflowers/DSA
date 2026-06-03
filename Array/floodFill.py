"""
## Explanation of the Flood Fill Solution

### 1. Approach Explanation

The provided solution for the "Flood Fill" problem implements a breadth-first search (BFS) algorithm to fill a connected region in a 2D image. The process can be summarized as follows:

- **Starting Point:** The function begins by noting the original color of the pixel at the starting coordinates `(sr, sc)`. This value is referenced later to determine which pixels should be changed.
  
- **Queue Initialization:** A queue (using `deque` from the collections module) is initialized with the starting pixel coordinates `(sr, sc)`. This queue will hold the pixels that need to be processed.

- **Direction Vectors:** A list of direction vectors, representing the four possible movements (up, down, right, left) within the image, is defined to help traverse adjacent pixels.

- **Visited Tracking:** A set is utilized to keep track of visited pixels; this prevents processing the same pixel multiple times.

- **Processing Loop:** As long as there are pixels in the queue:
  - Dequeue the front pixel.
  - Change its color to the specified new color.
  - For each adjacent pixel (using the direction vectors):
    - Calculate its coordinates.
    - If the pixel is within bounds, has not been visited, and has the original color, it gets added to the queue for later processing and marks it as visited.

- **Return the Modified Image:** Once all connected pixels have been filled, the modified image is returned.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** \( O(N) \)
  - Here, \( N \) represents the total number of pixels in the image (i.e., `rows * cols`). Each pixel may potentially be visited once during the BFS traversal.

- **Space Complexity:** \( O(N) \)
  - The space complexity arises from the queue and the visited set. In the worst case, if all pixels are connected and need to be processed, both the queue and the visited set can hold up to \( N \) pixels.

### 3. Efficiency of the Approach

This BFS approach for the flood fill solution is efficient because:

- **Direct Connectivity Check:** It directly checks adjacent pixels based on defined directions, ensuring that it only revisits pixels if they belong to the connected region with the original color. This minimizes unnecessary processing.

- **Iteration Without Recursion:** BFS uses an iterative approach rather than recursion, which helps prevent stack overflow errors for large images and maintains consistent memory usage.

- **Optimal Color Change:** The image is directly modified in-place, which avoids the need for additional data structures to copy states, thus conserving memory.

In summary, this solution effectively and efficiently fills a region of connected pixels in a 2D image using BFS, adhering to the constraints of the problem.

Runtime: undefined
Memory: 19288000
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_val = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque([(sr, sc)])
        rows = len(image)
        cols = len(image[0])
        visited = set()
        while queue:
            x, y = queue.popleft()
            image[x][y] = color

            for i, j in directions:
                nx = x + i
                ny = y + j
                if (nx, ny) in visited:
                    continue
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == starting_val:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return image
