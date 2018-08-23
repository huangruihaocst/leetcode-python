class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row, column = len(grid), len(grid[0])
        # up
        res += sum(1 if h > 0 else 0 for l in grid for h in l)
        # side
        res += sum(max(l) for l in grid)
        # front
        res += sum(max([grid[i][j] for i in range(row)]) for j in range(column))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[2,2,2],[2,1,2],[2,2,2]]))
