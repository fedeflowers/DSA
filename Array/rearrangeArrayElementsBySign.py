"""
## Explanation of the Approach

The provided solution rearranges an array of integers such that positive and negative numbers alternate in the output array. The key steps involved in the solution are:

1. **Initialization**: The solution first initializes an output array called `ans` with the same length as the input array `nums`. This array is initially filled with zeros.
  
2. **Pointer Setup**: Two pointers are used:
   - `pos_index`: This pointer tracks the current index for placing positive integers (initialized to 0, which refers to the 0th index).
   - `neg_index`: This pointer tracks the current index for placing negative integers (initialized to 1, which refers to the 1st index).

3. **Iteration Through the Input Array**: The solution iterates through each element in the given array `nums`:
   - If the current element is positive, it is placed in the position indicated by `pos_index`, and `pos_index` is then incremented by 2 to move to the next even index.
   - If the current element is negative, it is placed in the position indicated by `neg_index`, and `neg_index` is incremented by 2 to move to the next odd index.

4. **Return the Output**: Finally, after populating all indices, the constructed array `ans` is returned as the result.

## Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of elements in the input array. The algorithm processes each element of the array exactly once in the loop.

- **Space Complexity**: O(N) as well, because we are using an additional array `ans` of the same length as the input to store the rearranged elements.

## Why This Approach is Efficient

This approach is efficient for several reasons:

1. **Direct Placement**: By utilizing two separate pointers for positive and negative numbers, the algorithm is able to place elements directly into the correct positions without requiring additional operations like sorting or merging, which would add unnecessary time complexity.

2. **Single Pass**: The entire operation is completed in a single pass through the input array, which minimizes the number of iterations and keeps the process linear in terms of time complexity.

3. **Space Utilization**: Instead of using multiple temporary structures or collections to store intermediate results, the solution leverages a single output array that matches the required format, leading to more efficient use of space.

4. **Simplicity**: The logic remains straightforward and readable, making it easier to understand and maintain.

Overall, this solution effectively balances performance with simplicity, making it a well-suited approach for the problem of rearranging array elements by sign.

Runtime: undefined
Memory: 42204000
"""

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = [x for x in nums if x > 0][::-1]
#         neg = [x for x in nums if x < 0][::-1]
#         res = []
#         while len(pos) > 0 or len(neg) > 0:
#             res.append(pos.pop())
#             res.append(neg.pop())

#         return res

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initializing an answer array of size n
        ans = [0] * n

        # Initializing two pointers to track even and
        # odd indices for positive and negative integers respectively
        pos_index, neg_index = 0, 1

        for i in range(n):
            if nums[i] > 0:
                # Placing the positive integer at the
                # desired index in ans and incrementing pos_index by 2
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                # Placing the negative integer at the
                # desired index in ans and incrementing neg_index by 2
                ans[neg_index] = nums[i]
                neg_index += 2

        return ans
