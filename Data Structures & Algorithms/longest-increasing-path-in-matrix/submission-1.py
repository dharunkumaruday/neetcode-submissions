sys.setrecursionlimit(15000)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(matrix)
        n = len(matrix[0])

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            ans = 1

            for nx, ny in dxy:
                nx += i
                ny += j

                if nx >= 0 and ny >= 0 and nx < m and ny < n and matrix[nx][ny] > matrix[i][j]:
                    ans = max(ans, 1 + solve(nx, ny))
            
            memo[(i, j)] = ans

            return ans

        mmax = 0

        for i in range(m):
            for j in range(n):
                mmax = max(mmax, solve(i, j))

        return mmax
        

