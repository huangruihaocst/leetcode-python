class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return list()
        elif numRows == 1:
            return [[1]]
        else:
            res = [[1]]
            for _ in range(numRows - 1):
                new = list()
                n = len(res[-1])
                for i in range(n + 1):
                    if i == 0 or i == n:
                        new.append(1)
                    else:
                        new.append(res[-1][i] + res[-1][i - 1])
                res.append(new)
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
