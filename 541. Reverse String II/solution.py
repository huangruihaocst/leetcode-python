class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = str()
        while len(s) >= 2 * k:
            res += s[k - 1::-1] + s[k:2 * k]
            s = s[2 * k:]
        if len(s) < k:
            res += s[::-1]
        else:
            res += s[k - 1::-1] + s[k:]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr('abcdefg', 2))
