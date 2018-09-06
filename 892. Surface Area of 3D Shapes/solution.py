class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def surface(h):  # surface of a tower of h cubes
            if h == 0:
                return 0
            return 2 + 4 * h

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += surface(grid[i][j])
                if i > 0:
                    res -= min(grid[i - 1][j], grid[i][j]) * 2
                if j > 0:
                    res -= min(grid[i][j - 1], grid[i][j]) * 2
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
