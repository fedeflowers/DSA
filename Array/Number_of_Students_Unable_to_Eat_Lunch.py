"""
```markdown
## Explanation of the Solution for "Number of Students Unable to Eat Lunch"

### 1. Brief Explanation of the Approach

The solution uses a counting strategy to determine how many students are unable to eat lunch based on their preferences and the available sandwiches. The key steps are as follows:

- **Count Preferences**: The solution utilizes a `Counter` from the `collections` module to count the number of students preferring each type of sandwich (represented by 0s and 1s).
  
- **Evaluate Sandwiches**: The algorithm iterates through each sandwich in the `sandwiches` list. For each sandwich type, it checks the `counts` to see if there are any students who want that type of sandwich.
  
  - If there are students who desire the sandwich (`counts[s] > 0`), one student is allowed to eat, and both the count of that type of sandwich and the total count of remaining students are decremented.
  - If no student wants the current sandwich type (`counts[s] == 0`), it means no further sandwiches can be eaten by any students (as they are in a queue waiting), and the remaining number of students is returned immediately.

- **Final Return**: If all sandwiches are processed without finding an unconsumed sandwich, it returns 0, indicating that all students were able to eat.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(N), where N is the total number of students (or sandwiches). This is because we are iterating through each sandwich and performing constant-time operations (like counting updates) for each one.

- **Space Complexity**: The space complexity is O(1) for the counting table in the form of a `Counter`. Although `Counter` internally uses a dictionary to store count information, the maximum number of unique keys (0 and 1) is constant, resulting in negligible extra space use relative to input size.

### 3. Why This Approach is Efficient

This approach is efficient due to its linear traversal of the input lists and reliance on counting rather than complex data structures or nested loops. The use of a `Counter` allows quick access to student preferences and avoids repeatedly iterating through the `students` list, as seen in other possible solutions. This efficiency is crucial given that the problem may arise with large input sizes, allowing the algorithm to handle such cases promptly while providing an accurate count of the students unable to eat lunch.
```

Runtime: undefined
Memory: 17840000
"""

# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         students = Deque(students)
#         sandwiches = Deque(sandwiches)
#         while students and sandwiches and any(student == sandwiches[0] for student in students):
#             if students[0] == sandwiches[0]:
#                 students.popleft()
#                 sandwiches.popleft()
#             else:
#                 students.append(students.popleft())

#         return len(students)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count preferences (0s and 1s)
        counts = collections.Counter(students)
        
        remaining = len(students)
        
        for s in sandwiches:
            if counts[s] > 0:
                counts[s] -= 1
                remaining -= 1
            else:
                # No student wants this sandwich; no one else can eat
                return remaining
                
        return 0
