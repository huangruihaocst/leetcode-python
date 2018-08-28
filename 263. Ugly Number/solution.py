class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        for factor in [2, 3, 5]:
            while num % factor == 0:
                num //= factor
        if num == 1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(14))
