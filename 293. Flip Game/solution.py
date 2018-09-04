class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = list()
        for i in range(len(s) - 1):
            if s[i] == s[i + 1] == '+':
                res.append(s[:i] + '--' + s[i + 2:])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generatePossibleNextMoves('++++'))
