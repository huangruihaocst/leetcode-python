class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i, c in enumerate(s[::-1]):
            res += (ord(c) - ord('A') + 1) * 26 ** i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('ZY'))
