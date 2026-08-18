from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
                
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output