"""
## Explanation of the Solution for "Number of Visible People in a Queue"

### 1. Approach Explanation
The problem seeks to determine how many people each person in a queue can see if they look to their right. A person can see another person if they are taller than the individuals in between them. The solution employs a monotonic stack to efficiently track the visibility of people in the queue.

Here’s how it works:
- Iterate through the list of heights from right to left (back to front). This allows us to manage visibility from a perspective of the person currently being processed.
- Utilize a stack to maintain a list of heights that have been processed. Since the stack is monotonic decreasing, taller people (or the heights of people) will be at the bottom and shorter ones on top.
- For each height:
  - While there are still elements in the stack and the current height is greater than the height at the top of the stack, pop elements from the stack. Each pop indicates a visible person, and we count these.
  - After processing visibility:
    - If the stack is not empty, the current person can see the person at the top of the stack (which is the tallest in their direct line of sight).
    - Append the current height to the stack.
- Finally, the result is collected in reverse order and returned.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - Each height is pushed onto the stack and popped at most once. Thus, overall operations on the stack are proportional to the number of people, leading to O(N) time complexity.
  
- **Space Complexity**: O(N)
  - The space complexity primarily arises from the stack used to hold the heights, which could grow to be the size of the input list in the worst case.

### 3. Why This Approach is Efficient
This approach is efficient because it efficiently handles the visibility calculations with a single pass through the heights while tracking visible heights in a structured manner using a stack. The monotonic stack ensures that we only retain relevant heights, eliminating the need for nested loops that could lead to O(N²) complexity. This efficiently compares current and previous heights and guarantees that the solution will scale well even with larger inputs, maintaining linear time complexity.

Runtime: undefined
Memory: 31604000
"""

# class Solution:
#     def canSeePersonsCount(self, heights: List[int]) -> List[int]:
#         # se parto dalla fine, mi posso tenere una sorta di lista ordinata delle persone
#         # se una persona supera un'altra allora quella superata o quelle superate devono essere tolte, se è ordinata
#         # basta fare bin serach per vedere dove si posiziona l'individuo nella lista per osservare alla sua destra
#         # magari tipo heapq
#         # numero di persone che vede una persona = num nello heap 
        
#         def how_many(heap, element): # remove from heap and count removed, also add element to heap, min heap
#             removed = 0
#             while heap and heap[0] < element:
#                 heapq.heappop(heap)
#                 removed += 1
#             seen = removed + (1 if len(heap) >= 1 else 0)
#             heapq.heappush(heap, element)
#             return seen

        
#         n = len(heights)
#         ppl = []
#         res = []
#         for i in range(n-1, -1, -1):
#             res.append(how_many(ppl, heights[i]))
#         return res[::-1]

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = [] # Monotonic decreasing stack
        
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            # If stack is not empty, the person can see one more (the taller one blocking others)
            res[i] = count + (1 if stack else 0)
            stack.append(heights[i])
            
        return res
