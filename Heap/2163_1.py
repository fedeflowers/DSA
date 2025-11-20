#brute force

# class Solution:
#     # O(n choose k * (k for path copy))
#     def combinations(self, nums, k):
#         res = []
#         def _combine(start, path):
#             if len(path) == k:
#                 res.append(path[:])
#                 return

#             if start == len(nums):
#                 return

#             #take
#             path.append(nums[start])
#             _combine(start+1, path)
#             path.pop()
#             #not take
#             _combine(start+1, path)
#         _combine(0, [])
#         return res

#     def minimumDifference(self, nums: List[int]) -> int:
#         n = len(nums) // 3
#         res = float("inf")
#         for combination in self.combinations(nums, n):
#             removed = set(combination)
#             valid = []
#             for el in nums:
#                 if el not in removed:
#                     valid.append(el)

#             first_side = valid[:n]
#             second_side = valid[n:]
#             diff = sum(first_side) - sum(second_side)
#             res = min(res, diff)
#         return res



class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3, n = len(nums), len(nums) // 3

        part1 = [0] * (n + 1)
        # max heap
        total = sum(nums[:n])
        ql = [-x for x in nums[:n]]
        heapq.heapify(ql)
        part1[0] = total

        for i in range(n, n * 2):
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total

        # min heap
        part2 = sum(nums[n * 2 :])
        qr = nums[n * 2 :]
        heapq.heapify(qr)
        ans = part1[n] - part2

        for i in range(n * 2 - 1, n - 1, -1):
            part2 += nums[i]
            heapq.heappush(qr, nums[i])
            part2 -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2)

        return ans