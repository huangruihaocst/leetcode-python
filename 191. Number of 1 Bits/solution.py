class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1:
        # return bin(n)[2:].count('1')

        # Solution 2:
        res = 0
        while n > 0:
            res += 1
            n = n & (n - 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(11))
