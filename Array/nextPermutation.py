"""
## Explanation of the Next Permutation Solution

The "Next Permutation" problem involves rearranging a sequence of numbers into its next lexicographically greater permutation. If such a permutation does not exist (i.e., the array is sorted in descending order), we need to rearrange it to the lowest possible order (ascending). The provided solution implements this in-place, meaning it modifies the input array directly without using extra space.

### 1. Approach Explanation

The solution follows these main steps:

1. **Find the Pivot**: Start by scanning backward through the array to find the first element (`nums[i]`) that is smaller than the element next to it (`nums[i+1]`). This identifies the point at which the current permutation stops being increasing, meaning a "pivot" for the next permutation is found. 

2. **Find the Successor**: Once the pivot is identified, the next step is to find the smallest element to the right of the pivot that is larger than `nums[i]`. Represented by `nums[j]`, this ensures that swapping these two will yield the smallest next permutation.

3. **Swap and Reverse**: After the swap, the array elements to the right of the pivot index should be reversed. Since these elements were originally in descending order (to the right of `i`), reversing them will change them to ascending, which is the required order to achieve the next permutation.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of elements in the input list. The algorithm involves linear scans of the array (two passes) to locate the pivot and successor, and one pass to reverse the tail of the array.

- **Space Complexity**: O(1) because the algorithm modifies the list in place and does not use any additional data structures that grow with input size.

### 3. Why is this Approach Efficient?

This approach is efficient due to the linear time complexity and the in-place modification:

- **Direct Manipulation**: It manipulates the original array without additional space, making it optimal for large datasets.
- **Systematic Finding**: Rather than generating all permutations or using complex data structures, the solution directly identifies the next permutation via a clear set of operations. This minimizes unnecessary computations and simplifies the logic.
- **Guaranteed Result**: It systematically guarantees that the generated permutation is the next in the sequence, ensuring that no permutations are missed.

Overall, this method efficiently produces the next permutation with minimal overhead in time and space.

Runtime: undefined
Memory: 19232000
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        n = len(nums)
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1

        # If such an element exists (i.e., not the last permutation like 3,2,1)
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to swap with
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements after the pivot, then they will become from smallest to largest
        # If i was -1 (last permutation), this reverses the whole list
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

