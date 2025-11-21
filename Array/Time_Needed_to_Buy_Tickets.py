"""
# Explanation of LeetCode Solution for "Time Needed to Buy Tickets"

## 1. Approach Explanation

The solution utilizes a queue (specifically, a deque) to simulate a ticket-buying process where each person in line buys one ticket at a time. The algorithm operates as follows:

- **Initialization**: A deque is initialized with tuples containing the number of tickets each person has and their respective index in the input list.
  
- **While Loop**: The loop continues until the deque is empty:
  - A person (the first in line) is dequeued. Their ticket count is decreased by one, simulating the purchase of a ticket, and a time counter is incremented.
    
  - After the ticket purchase, the algorithm checks if the dequeued person is the target person (identified by index `k`) and whether they have no tickets left. If both conditions are true, the total time taken so far is returned as the result.
    
  - If the dequeued person still has tickets remaining, they are re-enqueued to get back in line.
  
The process continues until the target person successfully buys their tickets.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The worst-case time complexity is O(N), where N is the total number of tickets (sum of all tickets in the list). In the worst-case scenario, each person in the queue buys one ticket per iteration, and they may need to go through the queue multiple times. Thus, the total number of operations is proportional to the total number of ticket purchases.

- **Space Complexity**: The space complexity is O(N) due to the storage of the initial deque that contains all the tuples of ticket counts and their respective indices. This accounts for storing all the people initially in the queue.

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Simulation of Real Process**: It effectively simulates the actual ticket-buying process in a straightforward manner using a queue, which reflects the FIFO (First-In-First-Out) nature of people waiting in line.

- **Dynamic Handling**: By re-adding individuals with remaining tickets back to the queue, the algorithm dynamically adjusts to changes, ensuring that no person is skipped in the process.

- **Simpler Logic**: Compared to more complex algorithms, this solution’s logic is simpler and easier to understand, making it maintainable and less prone to errors.

Overall, this approach efficiently captures the dynamics of the problem while keeping the implementation straightforward and intuitive.

Runtime: undefined
Memory: 17644000
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = Deque([(t, i) for i, t in enumerate(tickets)])
        time = 0
        while q:
            tickets, index = q.popleft()
            time += 1
            tickets -= 1
            if index == k and tickets == 0:
                return time

            if tickets > 0:
                q.append((tickets, index))
        return -1
