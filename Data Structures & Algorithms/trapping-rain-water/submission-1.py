class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = height[0]
        rightMax = height[n-1]
        leftMaxTillCurrent = []
        rightMaxTillCurrent = []
        ans = 0


        for i in range(1, n):
            leftMaxTillCurrent.append(leftMax)
            leftMax = max(leftMax, height[i])
        
        for i in range(n-2, -1, -1):
            rightMaxTillCurrent.append(rightMax)
            rightMax = max(rightMax, height[i])

        rightMaxTillCurrent.reverse()

        for i in range(1, n-1):
            ans += max(0, min(leftMaxTillCurrent[i-1], rightMaxTillCurrent[i-1]) - height[i])

        return ans
