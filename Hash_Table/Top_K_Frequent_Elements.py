# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    return [item for item, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]