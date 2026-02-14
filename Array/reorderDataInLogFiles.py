"""
## Explanation of the LeetCode Solution for "Reorder Data in Log Files"

### 1. Approach Explanation
The solution involves two main steps: separating the logs into letter logs and digit logs, followed by sorting the letter logs. The key steps are as follows:

- **Separation of Logs**: The input list of logs is iterated through. Each log is split into an identifier (`id`) and the content. If the content starts with a digit, it is categorized as a digit log and stored separately. Otherwise, it is classified as a letter log and stored along with its identifier in a tuple format `(id, content)`.

- **Sorting Letter Logs**: The letter logs are then sorted primarily by their content, and secondarily by their identifier (in case of ties). This is achieved by utilizing Python's sort functionality with a custom key that returns a tuple `(content, id)` for each letter log.

- **Reconstruction of Logs**: After sorting, the letter logs are reformatted back into the original log string format by concatenating the identifier and content. Finally, the sorted letter logs are combined with the digit logs (which maintain their original order) and returned as the final result.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The algorithm iterates through the list of logs once to separate them into letter and digit logs, which takes O(N), where N is the number of logs.
  - Sorting the letter logs, which in the worst case can be up to N logs, takes O(M log M), where M is the number of letter logs. The overall complexity is dominated by the sorting step, making the total time complexity O(N log N).

- **Space Complexity**: 
  - The space complexity is O(N) because in the worst case, if all logs are letter logs, we store all of them in the `letter_logs` list. The `digits_logs` list also requires additional space, but it is at most O(N) as well.

### 3. Efficiency of the Approach
This approach is efficient for several reasons:

- **Clear Separation**: By categorizing the logs into letter and digit logs initially, the solution simplifies the sorting task, since sorting is only performed on the letter logs. This takes advantage of the stability of sorting and the fact that digit logs can remain in their original order without needing further processing.

- **Optimal Sorting**: Utilizing Python's built-in sort function, which is highly optimized, guarantees that the sorting of letter logs is performed efficiently with respect to time.

- **Simplicity and Readability**: The use of tuples for storing letter log pairs and the clear logical flow make the code straightforward and easy to understand.

In summary, this approach is effective because it efficiently organizes and sorts the logs while maintaining simplicity, resulting in clear and maintainable code.


Runtime: undefined
Memory: 19452000
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digits_logs = []
        
        for log in logs:
            id, content = log.split(' ', 1)
            if content and content[0].isdigit():
                digits_logs.append(log)
            else:
                letter_logs.append((id, content))
        
        letter_logs.sort(key = lambda x: (x[1], x[0]))
        letter_logs = [id + " " + content for id, content in letter_logs]
        
        return letter_logs + digits_logs
