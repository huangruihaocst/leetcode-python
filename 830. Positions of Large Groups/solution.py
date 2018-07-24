class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        curr, cnt = None, 0
        res = list()
        for i, c in enumerate(S):
            if c == curr:
                cnt += 1
            else:
                if cnt >= 3:
                    res.append([i - cnt, i - 1])
                curr = c
                cnt = 1
        if cnt >= 3:
            res.append([len(S) - cnt, len(S) - 1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largeGroupPositions('aaa'))
