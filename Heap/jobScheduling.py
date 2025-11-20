class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
        # 1,3, 20  - > 3, 1, 0+20
        # 2,5, 20
        # 3,10, 100 -> 10, 3, 120
        # 4,6, 70
        # 6,9, 60

        #___________brute-force_____________
        #T:2^n, M: n
        #bfs all options, bfs or dfs with index 
        # max_profit = 0
        # intervals = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        # intervals.sort()  # sort by start time

        # def backtrack(time, index, p):
        #     nonlocal max_profit
        #     for i in range(index, len(intervals)):
        #         if intervals[i][0] >= time:  # if the job starts at or after the current time
        #             max_profit = max(max_profit, p + intervals[i][2])
        #             backtrack(intervals[i][1], i + 1, p + intervals[i][2])

        #     return max_profit

        # return backtrack(0, 0, 0)

        #_______________optimize____________________
        # [(0,0),(0,0),(0,0),[0,0],0,0]
        # [[0,0], [3, 20],[5,20] [10, 120], [6, 90], [9, 150]]  iterate each time and take the first possible one
        # T: O(n**2), M: O(N)
        # intervals = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        # intervals.sort()  # sort by start time
        # best_overall = 0
        # dp = [[0,0] for _ in range(len(intervals)+1)]
        # for i in range(len(intervals)):
        #     s, e, p = intervals[i]
        #     best_p = p
        #     i = i+1
        #     for j in range(i-1, -1, -1):
        #         if s >= dp[j][0]:
        #             best_p = max(dp[j][1] + p, best_p)
        #             best_overall = max(best_p, best_overall)
        #             dp[i] = [e, best_p]  

        # return best_overall

        # Create a list of jobs and sort them by start time.
        jobs = sorted(zip(startTime, endTime, profit))
        
        # Initialize heap and max_profit.
        # Heap stores tuples: (end_time, profit)
        heap = []
        max_profit_so_far = 0
        
        for s, e, p in jobs:
            # Remove jobs from the heap that have ended by the current job's start time.
            # While there is at least one job that ended before s, update max_profit_so_far.
            while heap and heap[0][0] <= s:
                end_time, curr_profit = heapq.heappop(heap)
                max_profit_so_far = max(max_profit_so_far, curr_profit)
            
            # Add the current job: the accumulated profit if this job is taken.
            # Note: max_profit_so_far stores the best profit we could have before starting job s.
            heapq.heappush(heap, (e, max_profit_so_far + p))
        
        # After processing all jobs, some jobs might still be in the heap.
        # Their profit values are also potential answers.
        while heap:
            _, curr_profit = heapq.heappop(heap)
            max_profit_so_far = max(max_profit_so_far, curr_profit)
        
        return max_profit_so_far





        
