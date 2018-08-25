class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Solution 1:
        # def is_power(i):
        #     if i == 1:
        #         return True
        #     if i % 2 == 1:
        #         return False
        #     return is_power(i // 2)
        #
        # if n <= 0:
        #     return False
        # return is_power(n)

        # Solution 2:
        if n <= 0:
            return False
        return n == (n & -n)


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(6))
