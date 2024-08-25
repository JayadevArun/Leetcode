class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % 1000000007
        return dp[n-1]