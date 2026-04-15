"""
```markdown
## Explanation of the Solution

### Approach
The given solution solves the problem of finding the shortest distance to a target string in a circular array of words. The main idea is to simultaneously traverse the array in both clockwise and counterclockwise directions, comparing the elements at each position to the target string. 

The steps involved in the algorithm are as follows:
1. Initialize a variable `smallest` to a very large value (infinity) to keep track of the minimum distance found.
2. Determine the length of the `words` array (`n`).
3. Iterate from `0` to `n-1`, checking distances in both the left and right directions:
   - **Left Direction**: Calculate the index to the left using modulo to simulate the circular nature of the array.
   - **Right Direction**: Similarly, calculate the index to the right with modulo arithmetic.
   - If either index matches the target string, update `smallest` with the current distance if it's less than the current value of `smallest`.
4. After the loop, if `smallest` is still infinity, it indicates that the target is not found, and we return `-1`. Otherwise, return the `smallest` distance found.

### Time and Space Complexity
- **Time Complexity**: O(n)
  - The solution iterates through the array a maximum of `n` times, where `n` is the number of words in the array. Each check involves constant time operations, so the overall complexity remains linear.
  
- **Space Complexity**: O(1)
  - The solution uses a constant amount of additional space for variables (`smallest`, `n`, `l`, `r`), regardless of the input size.

### Efficiency of the Approach
This approach is efficient for several reasons:
1. **Direct Comparisons**: By checking both directions simultaneously, the algorithm ensures that it finds the nearest target with minimal iterations.
2. **Circular Nature Handling**: The use of modulo arithmetic neatly handles the wrap-around of indices without any additional data structures or complex logic.
3. **Single Pass**: The algorithm only requires a single pass over the list, making it efficient in terms of processing time.
4. **No Additional Data Structures**: The absence of any lists or sets to store intermediate results keeps the memory usage low, further improving the efficiency.

Overall, the algorithm is optimal for the problem and effectively leverages properties of modular arithmetic to handle the circular structure of the array.
```

Runtime: N/A
Memory: N/A
"""

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        #the fastes way it doing to right and to left then compare the smallest O(n)
        smallest = float("inf")
        n = len(words)

        for i in range(n): 
            # left
            l = (startIndex - i + n) % n
            if words[l] == target:
                smallest = min(smallest, i)

            # right
            r = (startIndex + i) % n
            if words[r] == target:
                smallest = min(smallest, i)

        return smallest if smallest != float("inf") else -1
