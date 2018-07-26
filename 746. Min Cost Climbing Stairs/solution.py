class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Solution 1：
        # dp = [0 for i in range(len(cost) + 1)]
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[len(cost)]

        # Solution 2：
        p0, p1 = 0, 0
        for i in range(2, len(cost) + 1):
            p0, p1 = p1, min(p0 + cost[i - 2], p1 + cost[i - 1])
        return p1


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
