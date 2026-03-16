"""
# Explanation of the LeetCode Solution for "Sliding Window Maximum"

## 1. Approach Explanation
The solution uses a double-ended queue (deque) to maintain the indices of the elements in the current sliding window in descending order. The key steps of the approach are as follows:

- **Maintain the Max Element**: For each new element (pointed to by `end`), we ensure that the largest element's index remains at the front of the deque. This is achieved by removing indices from the back of the deque while the current element is greater than the elements pointed to by those indices.
  
- **Remove Out-of-Bounds Indices**: If the index at the front of the deque is outside the bounds of the current window (greater than `end - k`), we discard it from the deque. This ensures that we only store indices of elements that are currently within the sliding window.

- **Store Results**: Once we have scanned through at least `k` elements (i.e., when `end` is at least `k-1`), we append the value of the maximum for the current window (which is `nums[window[0]]`, the element at the index stored at the front of the deque) to the results list.

This process efficiently computes the maximum for each sliding window as we iterate through the list.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N). Each element from the `nums` list will be processed at most twice: once when it's added to the deque and potentially once when it's removed. Thus, the total time complexity is linear with respect to the number of elements.

- **Space Complexity**: O(k). In the worst case, the deque can store up to `k` indices at once (if they are all in the current sliding window). Therefore, space usage is proportional to the size of the window.

## 3. Why This Approach is Efficient
This approach is efficient because:

- **Optimal Element Management**: By using a deque to maintain a list of indices, we can quickly determine the maximum in constant time O(1) by checking the front of the deque. Other methods (like using a priority queue) could lead to higher overhead due to maintaining order or additional data structures.

- **Single Pass**: The solution effectively makes a single pass through the input list while maintaining a manageable amount of state (the deque), leading to excellent performance in both time and space.

- **Reducing Redundant Comparisons**: By leveraging properties of the sliding window and keeping only relevant indices in the deque, we avoid redundant checks against previous elements, which boosts efficiency significantly.

Runtime: undefined
Memory: 35352000
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        for end in range(len(nums)):
            #keep the max el on top of window
            while window and nums[end] > nums[window[-1]]:
                window.pop()

            window.append(end)
            
            if window[0] < end-k+1:
                window.popleft()

            if end >= k-1:
                res.append(nums[window[0]])
        return res

