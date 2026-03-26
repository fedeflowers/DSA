"""
```markdown
# Explanation of the Missing Ranges Solution

## 1. Approach Explanation

The problem requires finding ranges of missing numbers in a given sorted list of integers, `nums`, between a defined inclusive range from `lower` to `upper`. The provided solution uses the following approach:

- **Initialization**: It starts by checking if the input list `nums` is empty. If it is, it returns the range from `lower` to `upper` as the only missing range.

- **Handling the range before the first element**: If `lower` is less than the first element of `nums`, it means there are missing numbers from `lower` to one less than the first element. This range is added to the `ranges` list.

- **Finding gaps between successive elements**: The solution iterates through the list `nums`, checking each pair of consecutive elements. If there is a gap greater than 1 between `nums[i]` and `nums[i+1]`, it means there are missing numbers in that interval. The missing range is formulated as `[nums[i] + 1, nums[i + 1] - 1]` and added to the `ranges`.

- **Handling the range after the last element**: Finally, if the last element of `nums` is less than `upper`, it indicates that there are numbers missing from the last element to `upper`. This range is also added to the `ranges`.

The method returns the complete list of missing ranges.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The algorithm runs in O(N), where N is the number of elements in the `nums` list. The solution involves a single pass through the list to identify missing ranges, making the approach efficient in terms of processing time.

- **Space Complexity**: The space complexity is O(M), where M is the number of missing ranges identified. This is because the `ranges` list stores the missing intervals, and the storage grows linearly with the number of missing ranges.

## 3. Efficiency of the Approach

This approach is efficient due to its linear pass through the sorted list of numbers, resulting in minimal computational overhead. It effectively minimizes the number of operations by avoiding nested loops or additional data structures; it directly computes missing ranges based on existing numbers. Since the problem only requires identifying missing ranges rather than constructing a complete list of numbers, the method optimally balances time and space utilization. Furthermore, it operates under the assumption that the input `nums` is already sorted, which simplifies the logic and prevents unnecessary sorting operations.

This combination of linear time complexity and efficient space usage ensures that the solution can handle large input sizes effectively.
```

Runtime: undefined
Memory: 19320000
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        
        ranges = []
        if lower < nums[0]:
            ranges.append([lower, nums[0] - 1])
            
        for i in range(len(nums) - 1):
            if nums[i] + 1 < nums[i + 1]:
                ranges.append([nums[i] + 1, nums[i + 1] - 1])
                
        if nums[-1] < upper:
            ranges.append([nums[-1] + 1, upper])
            
        return ranges
