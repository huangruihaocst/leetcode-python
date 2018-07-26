class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if -6 <= num <= 6:
            return str(num)

        def helper(n):  # n >= 7
            li = list()
            while n >= 7:
                li.append(n % 7)
                n //= 7
            li.append(n)
            return ''.join(map(str, li[::-1]))

        if num >= 0:
            return helper(num)
        else:
            return '-' + helper(-num)


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(-7))
