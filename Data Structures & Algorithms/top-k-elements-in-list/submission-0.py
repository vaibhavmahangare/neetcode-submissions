from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. Frequency map
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # 2. Bucket: index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # 3. Collect top k frequent elements
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
