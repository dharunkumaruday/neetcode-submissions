class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        curr = {}
        n = len(s)

        for letter in t:
            target[letter] = target.get(letter, 0) + 1

        matched = 0
        required = len(target)

        def check_freq_match():
            return matched == required

        l = 0
        r = 0

        ans = ""
        min_ans = 10**9 + 7

        while r < n:
            currElement = s[r]
            curr[currElement] = curr.get(currElement, 0) + 1

            if currElement in target and curr[currElement] == target[currElement]:
                matched += 1

            if check_freq_match():
                while l <= r and check_freq_match():
                    currLen = r - l + 1

                    if min_ans > currLen:
                        ans = s[l:r+1]
                        min_ans = currLen

                    left = s[l]
                    curr[left] -= 1

                    if left in target and curr[left] < target[left]:
                        matched -= 1

                    l += 1

            r += 1

        return ans