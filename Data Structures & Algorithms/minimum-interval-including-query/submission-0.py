import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by their start points
        intervals.sort(key=lambda x: x[0])
        
        # 2. Sort queries while keeping track of their original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        min_heap = []  # Will store tuples of: (interval_size, right_endpoint)
        ans = [-1] * len(queries)
        
        i = 0
        n = len(intervals)
        
        # 3. Process each query in sorted order
        for q, original_index in sorted_queries:
            
            # Push all intervals that start on or before the current query
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(min_heap, (size, r))
                i += 1
                
            # Remove intervals from the heap that end before the current query (expired)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
                
            # If the heap is not empty, the top element is the smallest valid interval
            if min_heap:
                ans[original_index] = min_heap[0][0]
            else:
                ans[original_index] = -1
                
        return ans