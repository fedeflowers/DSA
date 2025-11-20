# Problem: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

from collections import deque

def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    taken = 0

    while queue:
        curr = queue.popleft()
        taken += 1
        for neighbor in graph[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return taken == numCourses