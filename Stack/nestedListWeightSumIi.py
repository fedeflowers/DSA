"""
```markdown
# Nested List Weight Sum II Solution Explanation

## 1. Approach

The problem "Nested List Weight Sum II" requires calculating the sum of integers in a nested list, where the weight of an integer is determined by its depth in the nest. Integers at deeper levels of nesting are weighted less than those at shallower levels.

The solution employs a two-step approach:
- **Depth Calculation**: It traverses the nested list to calculate the depth of each integer. For each `NestedInteger` that is an integer, the method records its depth and value.
- **Weighted Sum Calculation**: After calculating the maximum depth, it uses this to compute the weighted sum. The weight for each integer is computed as `max_depth - depth + 1`.

The helper function `depth` implements a recursive depth-first search (DFS) where:
- If the current element is an integer, its depth is recorded.
- If the current element is a nested list, the function recursively processes its elements, increasing the depth count.

After gathering all integers and their respective depths, the solution calculates the final weighted sum based on the depths.

## 2. Time and Space Complexity

- **Time Complexity**: O(N)  
  Where N is the total number of integers in the nested list. This is because each integer is processed exactly once to determine its depth and value.

- **Space Complexity**: O(D)  
  Where D is the maximum depth of the nested list. This is due to the recursion stack used during the depth-first traversal. Additionally, we have O(N) space for storing depths and integers, but since N could be large compared to D, the dominant factor in space complexity is typically considered O(D).

## 3. Efficiency of the Approach

This approach is efficient because:
- It processes each integer only once, ensuring linear time complexity relative to the number of integers.
- The recursive depth-first traversal is straightforward and natural for processing nested structures, allowing for clean separation of concerns (depth calculation vs. weight calculation).
- The method of calculating weights using `max_depth - depth + 1` ensures correct weighting without needing additional iterations or complex logic.

In summary, this solution efficiently computes the nested list weight sum using a direct approach that leverages the structure of the problem for optimal performance.
```

Runtime: N/A
Memory: N/A
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depths = []
        integers = []
        def depth(nested_el, d): #return array depths
            if nested_el.isInteger():
                depths.append(d)
                integers.append(nested_el.getInteger())
                return 

            l = nested_el.getList()
            for el in l:
                depth(el, d+1)

            



        for el in nestedList:
            depth(el, 0)
        m = max(depths)
        res = 0
        for i in range(len(depths)):
            w = m - depths[i] + 1
            res += w * integers[i]
        return res
        
