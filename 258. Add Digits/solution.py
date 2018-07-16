class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, str(num)))
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))
