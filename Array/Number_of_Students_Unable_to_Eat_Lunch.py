"""
```markdown
### Explanation of the Solution for "Number of Students Unable to Eat Lunch"

1. **Approach Explanation:**
   - The solution leverages the fact that there are only two types of sandwiches (denoted by `0` and `1`), which correspond to the preferences of the students.
   - It uses a `Counter` from the `collections` module to count how many students want each type of sandwich.
   - The algorithm iterates through the `sandwiches` list:
     - For each sandwich type, it checks if there are any students who want that sandwich type by checking the counts.
     - If there are students who want the sandwich (`counts[s] > 0`), the count for that type of sandwich is decremented and the total number of remaining students is also decremented.
     - If there are no students left who want the current sandwich type, it means that none of the remaining students can eat because they will all reject this sandwich type, and it returns the count of remaining students.
   - If all sandwiches are served and no issues arise, it returns `0`, indicating all students have been able to eat.

2. **Time and Space Complexity Analysis:**
   - **Time Complexity:** O(N), where N is the total number of students. The algorithm goes through each sandwich exactly once.
   - **Space Complexity:** O(1) in terms of extra space, since the `Counter` will hold at most 2 entries (for two types of sandwiches). However, if we take the input size into account, the space used by the input lists `students` and `sandwiches` is O(N).

3. **Why This Approach is Efficient:**
   - The approach is efficient because it simplifies the problem by focusing only on the counts of preferences instead of manually simulating each sandwich consumption, thereby avoiding unnecessary iterations and handling of data structures like queues.
   - It directly calculates when to stop processing the sandwiches based on the preferences of the students, ensuring minimal operations and quick determination of the remaining students.
   - The use of a `Counter` provides O(1) access for checking the number of students preferring each sandwich type, making the solution straightforward and easy to follow.
```


Runtime: N/A
Memory: N/A
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
