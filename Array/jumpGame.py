"""
# Explanation of LeetCode Solution for "Jump Game"

## 1. Brief Explanation of the Approach
The solution uses a greedy approach to determine whether it's possible to reach the last index of the list `nums`, which represents the maximum jump lengths from each index. The key idea is to maintain a variable `dp` that keeps track of the furthest index that can be reached as we iterate through the elements of the list. 

- The algorithm starts with `dp` initialized to `nums[0]`, which is the maximum jump we can make from the first position.
- Then, we iterate through the list from index `1` to `n-1`.
- At each index `i`, we check if it is possible to jump to index `i` from any of the previous indices (i.e., if `dp` is greater than or equal to `i`). 
- If it is possible to reach `i`, we update `dp` to be the maximum of its current value and `nums[i] + i`, which represents the furthest index we can reach from index `i`.
- If `dp` is less than `i`, this means it's not possible to reach index `i`, and the function returns `False`.
- If we successfully iterate through the entire list without returning `False`, the function returns `True`, indicating we can reach the last index.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n)
  - The solution makes a single pass through the list `nums`, checking each index only once. Thus, the time complexity is linear in relation to the number of elements `n` in the list.

- **Space Complexity**: O(1)
  - The only extra space used is for the variable `dp`, which does not scale with the input size. Therefore, the space complexity is constant.

## 3. Why This Approach is Efficient
This approach is efficient due to the greedy strategy of maintaining the maximum reachable index instead of storing the states for all indices. By keeping just one variable (`dp`), it minimizes space usage and avoids unnecessary computations. The linear time complexity means that the solution can handle larger inputs swiftly without performance degradation, making it suitable for the constraints typically present in competitive programming environments like LeetCode.

Overall, this method optimally combines performance and resource efficiency, allowing it to effectively tackle the problem of determining if one can successfully jump to the last index of the array.

Runtime: undefined
Memory: 20184000
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[0] #i dont need a full array, just 1 preceding value
        for i in range(1, n):
            if dp >= i: #can i arrive to this index?
                dp = max(dp, nums[i] + i)
            else:
                return False
            
        return True
        
        
