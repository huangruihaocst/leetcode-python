class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        res = [[0 for i in range(C)] for j in range(R)]
        for i, row in enumerate(M):
            for j, p in enumerate(row):
                li = list()
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i + di < R and 0 <= j + dj < C:
                            li.append(M[i + di][j + dj])
                res[i][j] = sum(li) // len(li)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.imageSmoother([[1,1,1],
 [1,0,1],
 [1,1,1]]))