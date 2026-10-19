class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n  = len(cost) + 1
        # if len(cost) is 1 then cost[i]
        # if len(cost) is 2 then min(cost[0], cost[1])
        # otherwise cost you pay is += min(cost[i-1], cost[i-1])


        n = len(cost)
        dp = [0] * (n+1)


        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] +cost[i-2])
        return dp[n]

       


        