import random
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        unique = list(freq.keys())

        def quickselect(arr, target_idx):
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)
            pivot_freq = freq[pivot]

            # Partition the numbers based on their frequency relative to the pivot's frequency
            lows = [x for x in arr if freq[x] < pivot_freq]
            mids = [x for x in arr if freq[x] == pivot_freq]
            highs = [x for x in arr if freq[x] > pivot_freq]

            if target_idx < len(lows):
                # Target is in the lows partition
                return quickselect(lows, target_idx)
            elif target_idx < len(lows) + len(mids):
                # Target frequency is the pivot frequency (cutoff found)
                return mids[0]
            else:
                # Target is in the highs partition.
                # Adjust the target index to be relative to the 'highs' array.
                new_target_idx = target_idx - len(lows) - len(mids)
                return quickselect(highs, new_target_idx) 

        kth_most_freq = quickselect(unique, len(unique) - k)
        return [x for x in unique if freq[x] >= freq[kth_most_freq]] #solo perchè la risposta è generata unique
