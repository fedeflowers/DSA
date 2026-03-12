"""
```markdown
### Explanation of the "Product of Array Except Self" Solution

#### 1. Brief Explanation of the Approach
The goal of the problem is to return an array where each element is the product of all the numbers in the input array `nums`, except for the number at that index. The approach taken here involves two auxiliary lists (`left` and `right`) to store products and compute the final result without using division.

- The `left` list is used to store the cumulative product of elements to the left of each index. For any index `i`, `left[i]` contains the product of all elements `nums[0]` to `nums[i-1]`.
- The `right` list stores the cumulative product of elements to the right of each index. For any index `i`, `right[i]` contains the product of all elements `nums[i+1]` to `nums[n-1]`, where `n` is the length of `nums`.

The algorithm works in three phases:
1. Populate the `left` array.
2. Populate the `right` array.
3. Combine the `left` and `right` arrays to construct the result array `res`.

#### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n)  
  The algorithm makes three passes through the array: once to compute the `left` products, once to compute the `right` products, and once to compute the final result. Therefore, the overall time complexity is O(n), where n is the length of the input `nums`.

- **Space Complexity**: O(n)  
  The algorithm uses three additional arrays (`left`, `right`, and `res`) of length `n+1` or `n`, leading to a space complexity of O(n). However, this can be optimized to O(1) if we modify the `res` array directly and eliminate the `left` and `right` arrays.

#### 3. Why This Approach is Efficient
This approach is efficient for several reasons:
- **No Division**: It avoids division to compute the products, which is crucial in cases where the input array may contain zeros or if there are other constraints preventing division.
- **Single Pass Computation**: By separating the products into left and right arrays, we efficiently compute the required product in a linear time without the need for nested loops, which would result in quadratic time complexity.
- **Intuitive Separation**: The separation of the product calculation into left and right sides makes the logic straightforward and easy to understand. Each part builds upon the useful contribution of the products accumulated from either side of the index.

In summary, this solution is both time-efficient and logically structured, providing a clear and effective means of solving the problem without relying on division operations.
```

Runtime: undefined
Memory: 26784000
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 6 24 1
        # 24 24 12 4 1
        left = [1] * (len(nums) +1) 
        right = [1] * (len(nums) +1)
        res = [1] * len(nums)

        #caso in cui c'è 0 va a tutto 0 tranne dove c'è lo 0, se ce ne sono due va tutto a 0


        for i in range(len(nums)):
            left[i] = left[i-1] * nums[i]
            right[len(nums) - i -1] = right[len(nums) - i ] * nums[len(nums) - i -1]

        for i in range(len(nums)):
            res[i] = left[i-1] * right[i+1]

        return res
        


