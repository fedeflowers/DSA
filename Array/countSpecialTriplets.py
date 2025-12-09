"""
```markdown
## Explanation of the LeetCode Solution for "Count Special Triplets"

### 1. Approach Explanation

The goal of the problem is to count the number of special triplets `(i, j, k)` in the list `nums` such that `i < j < k` and `nums[i] * 2 = nums[j]` and `nums[j] * 2 = nums[k]`. The improved solution uses the properties of counting frequencies to optimize the search for such triplets. Here's the breakdown of the steps involved:

- **Initialize Counters**: A `Counter` is initialized for the entire list `nums` to keep track of frequencies of each element, which is referred to as `after`. This will help to count how many valid `k` values exist for each `j`.

- **Use a Dictionary for Previous Elements**: A `prev` dictionary is used to keep track of the frequencies of elements that have already been processed. This allows you to count valid `i` values for each `j`.

- **Iterate through the list**:
    - For each element `el` at index `i`:
        - Decrease its count in the `after` Counter since we've now processed it.
        - Calculate the contribution to the result by checking how many times `el * 2` appears as a potential `k` using the `after` Counter. This gives the number of valid `k` values.
        - Use the `prev` dictionary to count how many times `el` has appeared before, contributing to the count of valid `i` values.
        - Update the `prev` dictionary to include the current element `el`.

- **Output the Result**: Finally, return the result modulo `10^9 + 7` to handle large numbers.

This method reduces the complexity by efficiently counting potential triplet components during a single pass through the list.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
    - The outer loop runs `O(n)` as it iterates through each element in the list `nums`.
    - Each operation within the loop (checking `Counter` and updating dictionaries) is average `O(1)`.
    - Thus, the overall time complexity is \(O(n)\).

- **Space Complexity**: 
    - We use a `Counter`, which stores the frequency of each unique element in the list, and a dictionary `prev` for previously counted elements.
    - In the worst case, both the `Counter` and `prev` can grow to store all unique elements of `nums`, yielding space complexity of \(O(n)\) in the worst case.

### 3. Efficiency of the Approach

This approach is efficient because it reduces the need for nested loops that would lead to a quadratic time complexity \(O(n^2)\). By leveraging counting through a single pass and using hash maps (i.e., `Counter` and dictionaries), the solution minimizes redundant operations and takes advantage of constant time operations for lookups and updates.

Overall, this method significantly improves performance while maintaining clarity and correctness, making it suitable for larger input sizes.
```

Runtime: undefined
Memory: 41512000
"""

# class Solution:
#     def specialTriplets(self, nums: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#         res = 0
#         # O(n**2) -> understand for each how many doubles i have before and after the number += before * after
#         for i in range(len(nums)):
#             before = Counter(nums[:i])
#             after = Counter(nums[i+1:])
#             res += before[nums[i]*2] * after[nums[i]*2]

#         return res % MOD
        
#intuition for improvement: I can compute all frequencies at the start, then while going forward I can subtract to it, and it becomes the after, and then computing the prev as going
#O(n), O(n)
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        after = Counter(nums)
        prev = {}
        res = 0
        for i in range(len(nums)):
            el = nums[i]
            after[el] -= 1
            res += prev.get(el*2, 0) * after.get(el*2, 0)
            prev[el] = prev.get(el, 0) + 1

        return res % MOD
