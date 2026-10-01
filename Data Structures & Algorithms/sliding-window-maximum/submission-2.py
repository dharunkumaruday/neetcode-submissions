from collections import deque
from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        window = SortedList()
        res = []

        while r < len(nums):
            window.add(nums[r])

            if r - l + 1 == k:
                res.append(window[-1])
                window.remove(nums[l])
                l += 1

            r += 1
        
        return res