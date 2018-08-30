class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Solution 1: Newton's Method 1
        # x = int((num + 1) / 2)
        # while True:
        #     y = int((x + num / x) / 2)
        #     if abs(x - y) < 2:
        #         if x * x == num or y * y == num:
        #             return True
        #         else:
        #             return False
        #     else:
        #         x = y

        # Solution 2: Newton's Method 2
        x = int((num + 1) / 2)
        while x * x > num:
            x = int((x + num / x) / 2)
        return x * x == num


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 100):
        if s.isPerfectSquare(i):
            print(i)
