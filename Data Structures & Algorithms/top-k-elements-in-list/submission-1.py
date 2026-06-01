from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # Bucket: index = frequency, value = list of nums with that frequency
        fre = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            fre[cnt].append(num)
        
        res = []
        for i in range(len(fre) - 1, 0, -1):
            for num in fre[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res   # safety, though problem guarantees a valid answer