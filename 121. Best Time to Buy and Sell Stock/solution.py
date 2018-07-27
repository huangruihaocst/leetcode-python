class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        smallest = prices[0]
        res = 0
        for p in prices[1:]:
            res = max(res, p - smallest)
            if p < smallest:
                smallest = p
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
