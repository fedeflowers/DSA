"""
```markdown
## Explanation of the Solution for "Last Stone Weight"

### 1. Brief Explanation of the Approach
The problem "Last Stone Weight" can be summarized as follows: You have an array of stones, where each stone has a certain weight. When two stones collide, they smash into each other; if they have different weights, the heavier stone will remain while the lighter stone will be destroyed (possibly leading to a smaller stone if they have the same weight). The goal is to find out the weight of the last remaining stone.

This solution employs a max-heap (simulated using a min-heap with negative values) to always extract the two heaviest stones efficiently. Here’s how the code works:

- First, we negate the weights of the stones and store them in a new list called `new_stones`. This is done because Python's built-in `heapq` module implements a min-heap, and we want to simulate a max-heap behavior.
- We use `heapq.heapify` to convert the `new_stones` list into a heap.
- In a loop, as long as there are at least two stones left, we repeatedly:
  - Pop the two heaviest stones (which are the smallest negatives).
  - If they are equal, both stones are destroyed (continue).
  - If they are different, the difference of the two weights is pushed back onto the heap (as a negative value).
- Finally, if no stones remain, we return `0`. If there is one stone left, we return its weight (negated back to positive).

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The heap operations (insertion and extraction) each take \(O(\log N)\), where \(N\) is the number of stones.
  - Pushing back and popping two stones will take \(O(\log N)\) for each collision, and since we potentially perform this for every stone, the overall complexity is \(O(N \log N)\).
  
- **Space Complexity**: 
  - The space used by the `new_stones` list is \(O(N)\) since we store all the stones. Therefore, the space complexity is \(O(N)\).

### 3. Why This Approach is Efficient
This approach is efficient because it leverages the properties of heaps to manage the extraction of the two heaviest stones quickly, which is crucial for minimizing the number of operations needed. By maintaining the stones in a heap, we efficiently retrieve and remove the two largest stones logarithmically in time, rather than linearly checking all stones.

Using a max-heap prevents the need for repeated sorting or linear searching for the largest weights, which helps in achieving an optimal solution even for larger inputs. The strategy of always addressing the largest stones first ensures we adhere closely to the problem requirements, leading to the correct final answer with minimal overhead.
```

Runtime: undefined
Memory: 17760000
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-s for s in stones]
        heapq.heapify(new_stones)

        while new_stones and len(new_stones) >= 2:
            y = heapq.heappop(new_stones)
            x = heapq.heappop(new_stones)

            if x == y:
                continue
            else:
                heapq.heappush(new_stones, y-x)

        if len(new_stones) == 0:
            return 0
        return -new_stones[0] 
