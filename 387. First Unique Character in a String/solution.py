class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        times = dict()
        for c in s:
            times[c] = times[c] + 1 if c in times else 1
        for i, c in enumerate(s):
            if times[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar('loveleetcode'))
