import numpy as np
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = np.array(nums)
        vals, counts = np.unique(arr, return_counts=True)
        top_k_idx = np.argsort(counts)[::-1][:k]
        return vals[top_k_idx].tolist()