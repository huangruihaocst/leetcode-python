class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0:
            return False
        history = set()
        while True:
            s = 0
            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10
            if s == 1:
                return True
            if s in history:
                return False
            history.add(s)
            n = s


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(7))
