class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num >>= 2
        if num == 1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(2))
