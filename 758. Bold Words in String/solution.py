class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        import re
        marked = [False] * len(S)
        for word in words:
            start = [m.start() for m in re.finditer('(?=' + word + ')', S)]
            for s in start:
                for i in range(s, s + len(word)):
                    marked[i] = True
        res = ''
        bold = False
        for i, c in enumerate(S):
            if bold:
                if not marked[i]:
                    res += '</b>' + c
                    bold = False
                else:
                    res += c
            else:
                if marked[i]:
                    res += '<b>' + c
                    bold = True
                else:
                    res += c
        if bold:
            res += '</b>'
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.boldWords(["ab", "bc"], 'aabcd'))
