import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        # Global max heap to track all tasks by (priority, taskId)
        self.global_heap = []
        # Track valid tasks and their owners
        self.task_prio = {}  # taskId -> priority
        self.task_uid = {}   # taskId -> userId
        
        for uid, tid, priority in tasks:
            self.task_prio[tid] = priority
            self.task_uid[tid] = uid
            # Use negative values for max heap behavior
            heapq.heappush(self.global_heap, (-priority, -tid))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_prio[taskId] = priority
        self.task_uid[taskId] = userId
        heapq.heappush(self.global_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # Update the priority mapping
        self.task_prio[taskId] = newPriority
        # Add new entry to global heap (old entries become stale)
        heapq.heappush(self.global_heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        # Remove from mappings (heap entries become stale)
        self.task_prio.pop(taskId, None)
        self.task_uid.pop(taskId, None)

    def execTop(self) -> int:
        # Clean up stale entries from top and find the best valid task
        while self.global_heap:
            neg_prio, neg_tid = self.global_heap[0]
            priority, taskId = -neg_prio, -neg_tid
            
            # Check if this entry is stale
            if (taskId not in self.task_prio or 
                self.task_prio[taskId] != priority):
                heapq.heappop(self.global_heap)  # Remove stale entry
                continue
            
            # Found valid task with highest priority
            heapq.heappop(self.global_heap)
            userId = self.task_uid[taskId]
            
            # Remove from mappings
            self.task_prio.pop(taskId)
            self.task_uid.pop(taskId)
            
            return userId
        
        return -1
