# Problem: Task Scheduler
# Link: https://leetcode.com/problems/task-scheduler/

from collections import Counter

def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)
    freq = Counter(tasks)
    max_freq = max(freq.values())
    tasks_with_max_freq = sum(1 for count in freq.values() if count == max_freq)

    intervals = (max_freq - 1) * (n + 1) + tasks_with_max_freq
    return max(intervals, len(tasks))