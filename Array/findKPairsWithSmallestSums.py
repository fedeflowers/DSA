"""
# Explanation of the LeetCode Solution for "Find K Pairs with Smallest Sums"

## 1. Brief Explanation of the Approach

The problem at hand requires us to find the `k` pairs with the smallest sums from two given arrays, `nums1` and `nums2`. This solution employs a min-heap (priority queue) to efficiently extract the smallest sum pairs.

Here’s a step-by-step walkthrough of the algorithm:

- **Initialization**: 
  - An empty list `res` is initialized to store the result pairs.
  - A min-heap `pq` is created, which will store tuples of the form `(sum, index in nums1, index in nums2)`.
  
- **Heap Push**:
  - The first element (the pair with the smallest sum) formed by taking the first elements of both `nums1` and `nums2` is pushed onto the heap.

- **Visited Set**:
  - A set `visited` is maintained to keep track of indices that have already been processed, preventing duplicate pairs from being added to the heap.

- **Main Loop**:
  - While the min-heap is not empty and `k` pairs have not yet been found, the smallest element is popped from the heap.
  - This element is added to the `res` list as the current smallest sum pair.
  - The algorithm checks two potential pairs: 
    - The next number in `nums1` with the current number in `nums2` (if it exists and hasn't been processed).
    - The current number in `nums1` with the next number in `nums2` (if it exists and hasn't been processed).
  - Each valid pair is pushed to the heap, and the associated indices are added to the visited set.
  
- **Termination**:
  - The loop continues until `k` pairs have been collected, at which point the result is returned.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The worst-case complexity is `O(k log k)`. Each insertion and extraction operation in the heap takes `O(log k)`, and since we are looking for `k` pairs, we could potentially perform this operation `k` times.
  
- **Space Complexity**: 
  - The space complexity is `O(k)` for the heap to store at most `k` pairs, and `O(n + m)` for the visited set (where `n` and `m` are the lengths of `nums1` and `nums2`, respectively), though in practice, space will be primarily dominated by the heap when `k` is smaller than the lengths of the lists.

## 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Min-Heap Utilization**: Using a min-heap allows us to always retrieve the current smallest sum in logarithmic time. This is much more efficient than sorting the entire list of pairs, which would take `O(n * m log(n * m))` time.

- **Avoiding Duplicates**: By employing a `visited` set, we avoid inserting duplicate pairs into the heap, significantly reducing unnecessary computations.

- **Incremental Pair Exploration**: The algorithm only explores pairs that are promising (i.e., pairs that involve the current smallest pair instead of blindly creating all combinations). This locality for exploring adjacent indices helps to ensure we stay closer to the smallest sums.

Overall, this algorithm cleverly balances the need for efficiency with the requirement of finding only the `k` smallest sums, yielding optimal performance for this problem.

Runtime: undefined
Memory: 35388000
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

            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j+1))

            k-= 1

        return res
