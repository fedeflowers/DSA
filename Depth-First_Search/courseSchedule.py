"""
```markdown
### Course Schedule Problem Solution Explanation

1. **Approach Explanation:**
   The solution employs a topological sorting algorithm to determine if it's possible to finish all courses given the prerequisites. The key steps in the approach are:

   - **Build Adjacency List:** A directed graph is created using an adjacency list where each course points to the courses that depend on it.
   - **Track In-Degree:** An in-degree count is maintained for each course to keep track of how many prerequisites (or dependencies) each course has.
   - **Queue for Courses with No Dependencies:** A queue is initialized with courses that have an in-degree of zero, meaning they have no prerequisites. These are the courses that can be taken first.
   - **Process the Queue:** Courses are processed from the queue, and for each course taken, the in-degrees of its dependent courses are reduced. If a dependent course's in-degree reaches zero, it is added to the queue for processing.
   - **Count Completed Courses:** The total number of courses processed is counted. If this count matches the total number of courses, it indicates that it is possible to complete all courses, and the function returns `True`. Otherwise, it returns `False`.

2. **Time and Space Complexity Analysis:**
   - **Time Complexity:** O(V + E), where V is the number of courses (vertices in the graph), and E is the number of prerequisite pairs (edges in the graph). This is due to the need to construct the graph and process each vertex and edge once.
   - **Space Complexity:** O(V + E) for storing the adjacency list and in-degree count. The space occupied by the queue in the worst case can be O(V) as well.

3. **Efficiency of the Approach:**
   This approach is efficient because it effectively utilizes breadth-first search (BFS) to traverse the directed graph while ensuring that all dependencies are resolved before taking a course. The usage of in-degrees allows for quick identification of courses that can be taken next, minimizing unnecessary processing. Compared to depth-first search (DFS), which might require additional stack space for recursion, this method is cleaner and reduces the risk of stack overflow for a large number of courses. Additionally, it directly captures the essence of the problem by relating it to topological sorting, making it easier to reason about the order of course completion.
```

Runtime: undefined
Memory: 20444000
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # #find a cycle
        # adj_list = defaultdict(list)
        # for e, s in prerequisites:
        #     adj_list[s].append(e)

        # #return it i has cycle
        # def dfs(node, stack, visited ):
        #     if stack[node]:
        #         return True
        #     if visited[node]:
        #         return False
            
        #     visited[node] = True
        #     stack[node] = True

        #     for neigh in adj_list[node]:
        #         if dfs(neigh, stack, visited):
        #             return True

        #     stack[node] = False
        #     return False

        # stack = [False] * numCourses
        # visited = [False] * numCourses
        # for i in range(numCourses):
        #     if dfs(i, stack, visited):
        #         return False

        # return True


        #topological sorting
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        for e, s in prerequisites:
            adj_list[s].append(e)
            in_degree[e] += 1

        # start from indegree 0
        queue = deque()
        count = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            el = queue.popleft()
            count+=1
            for neigh in adj_list[el]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        return count == numCourses




