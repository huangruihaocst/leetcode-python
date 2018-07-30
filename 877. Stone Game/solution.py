class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # Solution 1:  # Dynamic Programming
        n = len(piles)
        from collections import defaultdict
        dp = defaultdict(lambda: 0)
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i, j] = -piles[i]
                else:
                    player = (j - i + 1) % 2
                    if player == 1:  # Lee's turn
                        dp[i, j] = min(dp[i + 1, j] - piles[i], dp[i, j - 1] - piles[j])
                    else:
                        dp[i, j] = max(dp[i + 1, j] + piles[i], dp[i, j - 1] + piles[j])
        return dp[0, n - 1] > 0

        # Solution 2:
        # return True


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGame([5, 3, 4, 5]))
