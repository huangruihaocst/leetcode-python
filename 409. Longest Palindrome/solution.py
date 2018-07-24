class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counter = Counter(s)
        res = 0
        has_center = False
        for v, c in counter.items():
            if c % 2 == 0:
                res += c
            else:
                if has_center:
                    res += c - 1
                else:
                    res += c
                    has_center = True
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('abccccdd'))
