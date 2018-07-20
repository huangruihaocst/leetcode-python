class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s, key=lambda c: ord(c))
        t = sorted(t, key=lambda c: ord(c))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference("abcd", "abcde"))
