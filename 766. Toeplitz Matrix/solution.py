class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        for row in range(m - 1, -1, -1):
            diag = set()
            r, c = row, 0
            diag.add(matrix[r][c])
            while True:
                r += 1
                c += 1
                if 0 <= r <= m - 1 and 0 <= c <= n - 1:
                    diag.add(matrix[r][c])
                else:
                    break
            if len(diag) > 1:
                return False
        for col in range(1, n - 1):
            diag = set()
            r, c = 0, col
            diag.add(matrix[r][c])
            while True:
                r += 1
                c += 1
                if 0 <= r <= m - 1 and 0 <= c <= n - 1:
                    diag.add(matrix[r][c])
                else:
                    break
            if len(diag) > 1:
                return False
        return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix([[1, 2], [2, 2]]))
