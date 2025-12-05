"""
```markdown
## Explanation of the Solution for "Count Partitions with Even Sum Difference"

### 1. Approach Explanation

The goal of the problem is to count the partitions of an array such that the difference between the sums of the two resulting partitions is even. 

The solution follows these steps:

- **Prefix Sum Calculation**: 
    - The solution starts by calculating the prefix sums of the input array `nums`. This sums up the elements cumulatively and stores these sums in the `prefix_sum` list. For instance, if `nums = [1, 2, 3]`, the `prefix_sum` would be `[1, 3, 6]`.
    
- **Finding Valid Partitions**:
    - The code iterates through the `prefix_sum`, using the current index `i` to find the left partition's sum (`left_sum`) and the right partition's sum (`right_sum`). The right sum is computed as the total sum of the array minus the `left_sum`.
    - The key condition checked is whether the difference between `left_sum` and `right_sum` is even: `(left_sum - right_sum) % 2 == 0`. If this condition holds true, it means that the difference is even, and the current partitioning is valid.

- **Counting Valid Partitions**:
    - Each time a valid partition is found, we increment the result count (`res`).

Finally, the result count is returned, depicting the number of valid partitions.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
    - The code has a time complexity of O(N), where N is the number of elements in the input array `nums`. This is due to the single loop to compute the prefix sums and another loop that runs to check the counts of valid partitions.

- **Space Complexity**:
    - The space complexity is also O(N) because of the `prefix_sum` list, which stores the cumulative sums. The additional space used by `res` and `curr_sum` is constant (O(1)).

### 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Linear Time Calculation**: By using the prefix sum method, the solution calculates the sums in linear time, enabling it to handle longer arrays without significant slowdowns.
  
- **Single Pass After Prefix Sum**: Instead of checking every possible partition or combinations of elements (which would result in higher complexity), it efficiently evaluates only relevant slices of the array using the prefix sums and a simple modulus check.

- **Direct Checks for Parity**: The modulus operation to check if the difference is even is very efficient and straightforward, making the overall procedure both easy to comprehend and implement.

By leveraging cumulative sums, the solution minimizes the necessary calculations and maintains efficiency, which is crucial for larger datasets.
```

Runtime: undefined
Memory: 17832000
"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum = []
        res = 0
        curr_sum = 0
        for el in nums:
            curr_sum += el
            prefix_sum.append(curr_sum)

        for i in range(len(prefix_sum)-1):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if (left_sum - right_sum) % 2 == 0:
                res += 1
        return res
