"""
```markdown
### Explanation of the LeetCode Solution for "Number of Visible People in a Queue"

1. **Brief Explanation of the Approach**:
   The solution involves iterating through a list of people's heights from the end to the beginning. For each person, it uses a min-heap to keep track of the heights of people who have been processed so far (i.e., those to the right of the current person). The heap allows the solution to quickly determine how many people the current person can see based on their height:
   - If a taller person appears, they will block the view of shorter people in front of them.
   - The `how_many` function counts how many people can be seen by popping elements from the heap until it finds a person that is shorter than the current one.
   - The current height is then added to the heap. The function returns the number of visible persons for the current individual based on how many were removed (i.e., shorter people who don't block their view) and whether there is still anyone left in the heap after removals.

2. **Time and Space Complexity Analysis**:
   - **Time Complexity**: The solution iterates over the list of heights once (O(N)), and for each height, it performs operations on the heap. The operation to pop from the heap can take O(log M), where M is the current size of the heap. In the worst-case scenario, in a linear fashion (if heights are in increasing order), we could be popping all elements, resulting in O(N log N). Overall, the time complexity of the approach is O(N log N).
   - **Space Complexity**: The space complexity is O(N) due to the storage needed for the heap and the results list. The heap will store, at most, N elements in the worst case.

3. **Why This Approach is Efficient**:
   This approach is efficient because it leverages a min-heap to maintain the active list of visible heights dynamically. Instead of recalculating the visibility for each person in a brute-force manner (which could entail O(N^2) complexity), the heap structure allows for efficient insertion and removal of heights with logarithmic time complexity. This results in a significant performance improvement, especially for larger input sizes.
```


Runtime: undefined
Memory: 33828000
"""

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # se parto dalla fine, mi posso tenere una sorta di lista ordinata delle persone
        # se una persona supera un'altra allora quella superata o quelle superate devono essere tolte, se è ordinata
        # basta fare bin serach per vedere dove si posiziona l'individuo nella lista per osservare alla sua destra
        # magari tipo heapq
        # numero di persone che vede una persona = num nello heap 
        
        def how_many(heap, element): # remove from heap and count removed, also add element to heap, min heap
            removed = 0
            while heap and heap[0] < element:
                heapq.heappop(heap)
                removed += 1
            seen = removed + (1 if len(heap) >= 1 else 0)
            heapq.heappush(heap, element)
            return seen

        
        n = len(heights)
        ppl = []
        res = []
        for i in range(n-1, -1, -1):
            res.append(how_many(ppl, heights[i]))
        return res[::-1]


