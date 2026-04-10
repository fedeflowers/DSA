"""
```markdown
## Explanation of the Solution for "Minimum Distance Between Three Equal Elements I"

### 1. Brief Explanation of the Approach
The given solution aims to find the minimum distance between any three equal elements in a list `nums`. To solve the problem, the approach involves the following steps:

- **Indexing and Sorting**: The solution creates a list of tuples (`nums_index`) where each tuple contains the value and its corresponding index in the original list. This list is then sorted first by the values and then by their indices.

- **Sliding Window**: The algorithm uses a sliding window of size 3 to examine consecutive entries in the sorted list. For each triplet in this window, it checks if the values are equal. If they are, it computes the distance among them using their original indices and keeps track of the minimum distance.

- **Returning the Result**: Finally, if a valid distance was found (i.e., if it was updated from infinity), it returns that minimum distance; otherwise, it returns -1 if no three equal elements exist.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The dominant operations are:
  - Creating the list of tuples: O(n)
  - Sorting the list: O(n log n)
  - Iterating through the sorted list with a fixed window size (3): O(n)
  
  Thus, the overall time complexity is O(n log n).

- **Space Complexity**: The additional space used to store the indices is O(n). 
  Therefore, the space complexity is O(n).

### 3. Why This Approach is Efficient
This approach is efficient due to its systematic organization:
- **Sorting**: By sorting based on both values and indices, the algorithm enables a streamlined way to find groups of three equal elements in sequence without needing nested loops.
- **Window Technique**: The use of a sliding window approach within a sorted list minimizes unnecessary comparisons and efficiently calculates potential distances.
- **Single Pass for Minimum Distance**: Since it only checks consecutive triplets, it limits the number of checks required, making it much faster than a brute-force method.

Overall, the solution leverages sorting and a sliding window technique to achieve an optimal balance between clarity and performance.
```

Runtime: undefined
Memory: 19596000
"""

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # save indices, sort by vlue and index, go in 3 by 3 window and search if its good or not and save res -Z final time O(nlogn)
        nums_index = [(v, i) for i, v in enumerate(nums)]
        nums_index.sort(key=lambda x: (x[0], x[1]))
        dist = float("inf")
        #window 3 by 3 sliding
        for i in range(len(nums_index)-2):
            val1 = nums_index[i][0]
            val2 = nums_index[i+1][0]
            val3 = nums_index[i+2][0]

            d1 = nums_index[i][1]
            d2 = nums_index[i+1][1]
            d3 = nums_index[i+2][1]

            if val1 == val2 == val3:
                #compute distance
                dist = min(dist, abs(d1 - d2) + abs(d2 - d3) + abs(d3 - d1))

        return dist if dist != float("inf") else -1

