class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Pad the array with 1s on both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Memoization table initialized to -1
        memo = [[-1] * n for _ in range(n)]
        
        def dfs(l: int, r: int) -> int:
            # If there are no balloons between l and r
            if l + 1 == r:
                return 0
            
            # Return cached result if already computed
            if memo[l][r] != -1:
                return memo[l][r]
            
            max_coins = 0
            # Try every balloon i as the last one to be burst in range (l, r)
            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                coins += dfs(l, i) + dfs(i, r)
                max_coins = max(max_coins, coins)
                
            memo[l][r] = max_coins
            return max_coins

        # Solve for the entire padded range
        return dfs(0, n - 1)