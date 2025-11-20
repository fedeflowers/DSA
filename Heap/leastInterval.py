class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        cooldown = Deque()
        pq = []
        time = 0

        for task in tasks:
            freqs[task] = freqs.get(task, 0) + 1

        for key, freq in freqs.items():
            heapq.heappush(pq, (-freq, key))

        while pq or cooldown:
            time += 1
            if pq:
                freq, letter = heapq.heappop(pq)

            #add to cooldown
            freq += 1
            if freq < 0:
                cooldown.append((time +n, (freq, key)))#first available time
         
            #process if possible
            if cooldown and cooldown[0][0] == time:
                _, el = cooldown.popleft()
                heapq.heappush(pq, el)

        return time