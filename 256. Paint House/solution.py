class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [costs[0]]
        for i, cost in enumerate(costs):
            if i == 0:
                continue
            curr = list()
            curr.append(min(dp[i - 1][1], dp[i - 1][2]) + cost[0])
            curr.append(min(dp[i - 1][0], dp[i - 1][2]) + cost[1])
            curr.append(min(dp[i - 1][0], dp[i - 1][1]) + cost[2])
            dp.append(curr)
        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
