"""
## Next Permutation Solution Explanation

### 1. Brief Explanation of the Approach

The provided solution implements an algorithm to find the next lexicographical permutation of a list of integers `nums`. The algorithm follows these steps:

- **Step 1: Identify Pivot**
  - Start from the end of the list and move leftwards to find the first index `i` such that `nums[i] < nums[i + 1]`. This index `i` identifies the point where the increasing order breaks (the "pivot").

- **Step 2: Find Successor and Swap**
  - If such a pivot index `i` exists, find the smallest number in the suffix (the part of the list after `i`) that is greater than `nums[i]`, which we denote as `nums[j]`. Swap `nums[i]` with `nums[j]`. This ensures we increase the permutation.

- **Step 3: Reverse Suffix**
  - Finally, reverse the order of the elements to the right of index `i` (the suffix). This transforms the decreasing order into an increasing order, giving us the next permutation in lexicographical order.

If no valid pivot is found (meaning the entire array is in decreasing order), the array is sorted in its maximum permutation order, and we can simply reverse the entire array to return to the minimum permutation.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** O(N)
  - The algorithm consists of a linear scan to find the pivot (`O(N)`), a linear scan to find the element to swap (`O(N)`), and another linear scan to reverse the suffix (`O(N)`). Therefore, the overall time complexity is O(3N), which simplifies to O(N).

- **Space Complexity:** O(1)
  - The algorithm modifies the input list in-place without using any additional data structures. Therefore, the extra space used is constant, leading to a space complexity of O(1).

### 3. Why This Approach is Efficient

This approach is efficient because:
- It only requires a constant amount of additional space and iterates through the list a limited number of times, keeping the time complexity linear.
- The algorithm is designed to efficiently transition from one permutation to the next without generating all permutations, thus significantly reducing computational overhead.
- It effectively handles edge cases, ensuring that if the sequence is already in descending order (largest permutation), it can swiftly revert to the smallest permutation, offering a seamless user experience. 

Overall, this method strikes a balance between clarity, efficiency, and optimal resource usage, making it a preferred choice for solving the next permutation problem.

Runtime: undefined
Memory: 19344000
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1: vado in ordine crescente da dx finchè non si interrompe la streak
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-= 1

        #2: trovo da dx il primo più grande e lo swappo (prima era ordine decrescente quindi sono già ordinato da dx)
        if i >= 0: #altrimenti sono tutti in ordine decr
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]

        #3: faccio reverse dal pivot in poi, se è tutto in ordine decrescente, torno alla prima perm.
        left = i+1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
