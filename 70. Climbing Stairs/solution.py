class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1:
        # if n == 1:
        #     return 1
        # d = [0] * (n + 1)
        # d[1], d[2] = 1, 2
        # for i in range(3, n + 1):
        #     d[i] = d[i - 1] + d[i - 2]
        # return d[n]

        # Solution 2:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
