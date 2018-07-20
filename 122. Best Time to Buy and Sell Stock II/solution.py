class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i, p in enumerate(prices):
            if i < len(prices) - 1:
                if p < prices[i + 1]:
                    res += prices[i + 1] - p
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 6, 4, 3, 1]))
