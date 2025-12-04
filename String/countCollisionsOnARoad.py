"""
```markdown
## Explanation of the Solution for "Count Collisions on a Road"

### 1. Brief Explanation of the Approach

The problem requires us to count the number of collisions among cars moving left ('L'), right ('R'), or staying ('S'). The collisions only occur as follows:
- A right-moving ('R') car collides with a left-moving ('L') car when they meet.
- If a 'R' car meets an 'S' car, the 'R' car will collide and then turn into an 'S'.
- If an 'L' car meets an 'S' car, the 'L' car will collide and then turn into an 'S'.

The solution uses a stack to simulate the movement of the cars on the road:
- Traverse each car's direction in the input string.
- Depending on the current direction and the direction of the last car in the stack, we determine if a collision occurs.
- Collisions are counted, and the directions of the cars are updated as collisions occur.
- If collisions affect the car direction, they are represented as 'S' in the stack.

#### Key Steps in the Code:
1. Iterate through each car in the input string `directions`.
2. Check the conditions for collisions based on the last car in the stack and update the collision count accordingly.
3. Update the stack based on the results of the collisions (either pushing 'S' or the original car direction).
4. Return the total count of collisions after processing all cars.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The solution runs in O(n), where n is the length of the `directions` string. This is because we make a single pass through the input string, and operations on the stack (push/pop) are O(1).
- **Space Complexity**: The space complexity is O(n) in the worst case since, in the scenario where no collisions occur and all cars might be added to the stack, we may end up storing all characters.

### 3. Why This Approach is Efficient

This approach is efficient due to:
- The use of a stack allows us to dynamically track the state of the cars and handle collisions in a straightforward manner.
- The linear complexity ensures that even at maximum input size, the algorithm runs efficiently without unnecessary re-evaluations or nested loops.
- The simplicity of the logic — handling collisions directly as they occur, rather than requiring additional loops or data structures to analyze the entire input, keeps the solution both clear and performant.

Overall, the combination of a linear traversal and a stack to manage state makes this approach optimal for the problem at hand.
```

Runtime: undefined
Memory: 19372000
"""

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        for car in directions:
            collision = False
            if stack and car == "L":
                if stack[-1] == "S":
                    collision = True
                    collisions += 1
                    stack.pop()
                    car = "S"
                elif stack[-1] == "R":
                    collision = True
                    collisions += 2
                    stack.pop()
                    car = "S"
            while stack and car == 'S' and stack[-1] == "R":
                stack.pop()
                collisions += 1
                collision = True

            if collision == True:
                stack.append("S")
            else:
                stack.append(car)
            
            # print(stack, collisions, car)
                    
                    
        return collisions
            
