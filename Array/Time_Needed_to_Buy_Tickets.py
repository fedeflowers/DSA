"""
# Explanation of the LeetCode Solution for "Time Needed to Buy Tickets"

## 1. Brief Explanation of the Approach
The problem requires finding out how much time it will take for a person, standing at position `k` in a queue, to buy their tickets when the queue is represented by a list of integers (`tickets`), where each integer indicates the number of tickets each person in front has to buy. 

The approach taken in the solution is as follows:
- The solution calculates the total time taken for each person in the queue to buy their tickets using simple arithmetic. 
- It initiates a variable `total`, which will accumulate the total time spent at the counter.
- The target refers to the number of tickets the person at position `k` in the queue has.
- The solution iterates through the `tickets` list:
  - If the current person's index is less than or equal to `k`, it adds the lesser of their ticket count or the target ticket count to `total`.
  - If the current person's index is greater than `k`, it adds the lesser of their ticket count or one less than the target, since the target person will finish buying their tickets before those behind them can fully count the target's tickets.
- At the end of the iteration, `total` reflects the total time taken for the person at index `k` to acquire their tickets.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the total number of people in the queue. The solution involves a single loop that goes through the list of tickets once.
- **Space Complexity**: O(1), as the solution only uses a fixed amount of space (for the `total` and `target` variables) regardless of input size. The solution does not use any additional data structures whose size grows with input.

## 3. Why This Approach is Efficient
This approach is efficient for a couple of reasons:
- It avoids the need for a queue or deque data structure, simplifying the logic and removing the overhead of managing a queue.
- Instead of simulating the ticket buying process, which can involve many iterations and increases time complexity (as seen in some alternative approaches), it computes the total time directly through iteration and conditional checks.
- By only making a single pass through the list and using minimal additional storage, it maximizes performance in both speed and memory usage, making it suitable for larger inputs.

Overall, the solution efficiently calculates the required time in a straightforward manner while adhering to optimal time and space complexities.

Runtime: undefined
Memory: 17656000
"""

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         q = Deque([(t, i) for i, t in enumerate(tickets)])
#         time = 0
#         while q:
#             tickets, index = q.popleft()
#             time += 1
#             tickets -= 1
#             if index == k and tickets == 0:
#                 return time

#             if tickets > 0:
#                 q.append((tickets, index))
#         return -1

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        target = tickets[k]
        
        for i, t in enumerate(tickets):
            if i <= k:
                total += min(t, target)
            else:
                total += min(t, target - 1)
                
        return total
