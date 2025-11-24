"""
# Explanation of the LeetCode Solution for "Buildings With an Ocean View"

## 1. Brief Explanation of the Approach

The problem "Buildings With an Ocean View" requires us to identify buildings that can see the ocean. A building can see the ocean if there are no taller buildings to its right. The solution uses a stack to efficiently keep track of the indices of buildings that have an ocean view as we traverse the list of building heights from left to right.

Here's how the solution works step-by-step:
- We loop through each building's height using its index.
- If the current building is taller than the building indexed at the top of the stack, it means the building at the top of the stack cannot have an ocean view, so we pop it off the stack.
- We continue this process until we find a taller building or the stack is empty.
- Finally, we add the index of the current building to the stack because it might have an ocean view.
- The buildings that have an ocean view will be represented by the indices stored in the stack after the loop completes.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - We iterate through the list of buildings once. Each building is either added to or removed from the stack at most once, leading to a total of O(N) operations.
  
- **Space Complexity**: O(N)
  - In the worst case, where all buildings are in increasing height order, all indices could be stored in the stack leading to O(N) space usage.

## 3. Why This Approach is Efficient

This approach uses a stack to keep track of buildings with potential ocean views and efficiently evaluates each building against the last building on the stack. This optimizes the process as instead of checking every building to the right of the current building for height comparisons, we can quickly pop elements from the stack that cannot see the ocean. The combination of a single pass through the list of heights and the stack's LIFO (last-in-first-out) property allows us to efficiently determine which buildings have a view without unnecessary comparisons. This leads to an O(N) time complexity which is optimal for this type of problem.

Runtime: N/A
Memory: N/A
"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i, el in enumerate(heights):
            while stack and heights[stack[-1]] <= el:
                stack.pop()
            stack.append(i)

        return stack
