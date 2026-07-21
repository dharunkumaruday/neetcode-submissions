class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        memo = {}

        def solve(i, j):
            if j == m:
                return 1
            
            if i == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = 0

            if(s[i] == t[j]):
                ans += solve(i+1, j+1)

            ans += solve(i+1, j)

            memo[(i, j)] = ans

            return ans

        return solve(0, 0)