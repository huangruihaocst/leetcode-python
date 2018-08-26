class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_power(i):
            if i == 1:
                return True
            if i % 3 != 0:
                return False
            return is_power(i // 3)

        if n <= 0:
            return False
        return is_power(n)


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(3982))
