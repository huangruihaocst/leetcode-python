class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, c in enumerate(s):
            if i < len(s) - 1:
                if d[c] >= d[s[i + 1]]:
                    res += d[c]
                else:
                    res -= d[c]
            else:
                res += d[c]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))