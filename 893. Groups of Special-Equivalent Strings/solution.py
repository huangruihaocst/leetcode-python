class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def s_hash(string):
            odd, even = 1, 1
            for i, c in enumerate(string):
                if i % 2 == 0:
                    even *= ord(c)
                else:
                    odd *= ord(c)
            return even * 100 + odd

        d = dict()
        for s in A:
            h = s_hash(s)
            d[h] = d[h] + 1 if h in d else 1
        return len(d)


if __name__ == '__main__':
    s = Solution()
    print(s.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))
