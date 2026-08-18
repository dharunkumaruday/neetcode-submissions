from collections import defaultdict


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      # Build adjacency list in reverse sorted order so we can pop the smallest lexicographically
      graph = defaultdict(list)
      for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

      res = []

      def dfs(curr):
        while graph[curr]:
          dfs(graph[curr].pop())
        res.append(curr)

      dfs("JFK")
      return res[::-1]