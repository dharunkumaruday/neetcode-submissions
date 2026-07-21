class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        memo = {}

        def solve(index1, index2):
            if (index1, index2) in memo:
                return memo[(index1, index2)]

            if index1 == n and index2 == m:
                return True

            if index1 == n and index2+2 == m and p[index2+1] == '*' :
                return True
            
            if index1 == n or index2 == m:
                return False

            ans = False

            if p[index2] == '.':
                if index2 + 1 < m and p[index2+1] == '*':
                    ans = ans or solve(index1 + 1, index2)
                    ans = ans or solve(index1, index2 + 2)
                else:
                    ans = ans or solve(index1 + 1, index2 + 1)
            elif index2 + 1 < m and p[index2+1] == '*':
                if s[index1] == p[index2]:
                    ans = ans or solve(index1 + 1, index2)
                ans = ans or solve(index1, index2 + 2)
            elif s[index1] == p[index2]:
                ans = ans or solve(index1 + 1, index2 + 1)

            memo[(index1, index2)] = ans

            return ans
            
        return solve(0, 0)

            