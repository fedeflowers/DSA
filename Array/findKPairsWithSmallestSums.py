"""
```markdown
# Explanation of "Find K Pairs with Smallest Sums" Solution

## 1. Approach Explanation
The solution utilizes a min-heap (priority queue) to efficiently find the k smallest pairs from two sorted arrays, `nums1` and `nums2`. The pairs are formed by taking one element from each array such that their sum is minimized.

- **Initialization**: 
  - We start by pushing the initial pair `(nums1[0] + nums2[0], 0, 0)` into the heap. This tuple includes the sum and the indices of the respective elements in `nums1` and `nums2`.
  - A `visited` set is used to keep track of pairs of indices that have already been processed to avoid duplicates.

- **Main Loop**: 
  - With a while loop, we continue until the priority queue is empty or we have found k pairs.
  - For each iteration, we pop the smallest element from the heap, which gives us the current smallest sum and its corresponding indices.
  - We then push the next possible pairs into the heap:
    - Move down in `nums1` by increasing the index of `nums1` (i.e., `(i + 1, j)`).
    - Move right in `nums2` by increasing the index of `nums2` (i.e., `(i, j + 1)`).
  - If these new index pairs have not been visited yet, they are added to the heap and marked as visited.
  
- **Output**: After k iterations, we return the list of pairs found.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(k log k)
  - The `heappop` and `heappush` operations on the heap take O(log k) time, and since we are pushing at most k pairs to the heap, the overall complexity for pulling k smallest pairs becomes O(k log k).

- **Space Complexity**: O(k)
  - The space complexity mainly comes from the heap and the `visited` set which can hold at most k pairs.

## 3. Efficiency of the Approach
This approach is efficient because:
- It leverages the properties of the min-heap to always expand the current smallest sum, thereby ensuring we generate pairs in increasing order of their sums without having to generate all possible pairs beforehand.
- The `visited` set ensures we avoid processing the same index combination multiple times, reducing unnecessary computations.
- The algorithm operates well within expected time limits for large inputs, especially since it only explores relevant candidates for the smallest pairs based on sorted input arrays.

Overall, this method is both focused and systematic, ensuring both clarity and performance.
```

Runtime: undefined
Memory: 35520000
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        pq = []

        heapq.heappush(pq, (nums1 + nums2, 0, 0))
        i,j = 0,0
        visited = set()
        visited.add((i, j))
        while pq and k > 0 :
            _, i, j= heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            #Without the visited set, the pair at indices (1, 1) would be added to the heap twice:

            # Once when you are at (0, 1) and move Down.

            # Once when you are at (1, 0) and move Right.
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j+1))

            k-= 1

        return res
