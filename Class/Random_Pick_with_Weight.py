import random
from typing import List

class Solution:
    #bruteforce
    # def __init__(self, w: List[int]):
    #     #might be too heavy on memory
    #     std = []
    #     for i, val in enumerate(w):
    #         curr = [i] * val
    #         std += curr
    #     self.standardized = std

    # def pickIndex(self) -> int:
    #     return random.choice(self.standardized)


    #using python random
    # def __init__(self, w: List[int]):
    #     self.w = w
    #     self.sample = range(len(self.w))

    # def pickIndex(self) -> int:
    #     return random.choices(self.sample, weights = self.w)[0]



    # ok with thresholds
    # def __init__(self, w: List[int]):
    #     pr = []
    #     self.weights = sum(w)
    #     curr_val = 0
    #     for i, val in enumerate(w):
    #         curr_val += val
    #         pr.append((curr_val-1, i))
    #     self.prefix_sum = pr

    #linear search but they are in order!
    # def pickIndex(self) -> int:
    #     num = random.randint(0, self.weights-1)
    #     for el, sample in self.prefix_sum:
    #         if num <= el:
    #             return sample
        

    # w = [1, 3, 5]
    # [(0, 0), (3, 1), (8, 2)] <- in ordine la esplore e appena trovo un el >= di quello appena uscito ritorno il sample
    #prefix sum + random el



    #prefix sum + bin search
    def __init__(self, w: List[int]):
        pr = []
        self.weights = sum(w)
        curr_val = 0
        for val in w:
            curr_val += val
            pr.append(curr_val-1)
        self.prefix_sum = pr

    def pickIndex(self) -> int:
        num = random.randint(0, self.weights-1)
        l = 0
        r = len(self.prefix_sum) - 1
        res = 0
        while l <= r:
            middle = (l+r) // 2
            if num <= self.prefix_sum[middle]:
                res = middle
                r = middle - 1
            else:
                l = middle + 1

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
