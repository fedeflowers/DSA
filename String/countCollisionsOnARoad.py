"""
```markdown
# LeetCode Solution Explanation: Count Collisions on a Road

## 1. Brief Explanation of the Approach

The solution to the "Count Collisions on a Road" problem utilizes a straightforward approach by focusing on the significant parts of the `directions` string. The main steps are:

- **Trim the Input:** The code begins by removing all 'L' characters from the start of the string and all 'R' characters from the end. This is because any 'L' at the start will not cause a collision with any cars and similarly, 'R' at the end will never collide with others. Effectively, we focus on cars in the middle that might intersect paths.

- **Count Collisions:** After trimming, the cars remaining in the `trimmed` string can either be 'S' for stopped, 'L' for left, or 'R' for right. The remaining collisions are counted as any remaining 'L' or 'R' cars will inevitably collide with the 'S' cars (since 'L' will collide with a car going right and also with stopped cars that block its path).

- **Calculate Results:** The solution utilizes the length of the `trimmed` string minus the count of 'S' characters, as all cars that are 'L' or 'R' would contribute to a collision, and we are left only with accumulated collisions from those directions.

## 2. Time and Space Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(N), where N is the length of the `directions` string. The trimming operation (with `lstrip` and `rstrip`) and counting of 'S' involves scanning the string linearly, resulting in a one-pass operation.

- **Space Complexity:** The space complexity is O(N) due to the creation of a new string (`trimmed`). Although it does not use extra space for intermediate data structures, the `trimmed` string holds a modified version of the input string which might be up to N characters in length.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Simplicity:** By eliminating obvious non-colliding portions of the input string, it simplifies the problem, allowing us to focus only on parts that might cause collisions.

- **Linear Processing:** The use of linear time complexity means that even for large values of N, the solution can calculate the result quickly as it requires only two passes over the string for counting and trimming operations.

- **Minimal Logic:** The code avoids the need for complex data structures or iterative collision checks (which were present in the first solution). Instead, it relies on straightforward string manipulation and simple arithmetic to achieve the result, enhancing clarity and maintainability.

Overall, the approach directly addresses the core requirements of the problem in a clear and concise manner while maintaining optimal performance.
```

Runtime: undefined
Memory: 17952000
"""

# my solution
# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         stack = []
#         collisions = 0
#         for car in directions:
#             collision = False
#             if stack and car == "L":
#                 if stack[-1] == "S":
#                     collision = True
#                     collisions += 1
#                     stack.pop()
#                     car = "S"
#                 elif stack[-1] == "R":
#                     collision = True
#                     collisions += 2
#                     stack.pop()
#                     car = "S"
#             while stack and car == 'S' and stack[-1] == "R":
#                 stack.pop()
#                 collisions += 1
#                 collision = True

#             if collision == True:
#                 stack.append("S")
#             else:
#                 stack.append(car)               
                    
#         return collisions
            

# GEMINI:
class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove 'L's from the start and 'R's from the end
        trimmed = directions.lstrip('L').rstrip('R')
        # All remaining 'L' and 'R' cars will eventually collide
        return len(trimmed) - trimmed.count('S')
