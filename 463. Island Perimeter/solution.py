class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        y, x = len(grid), len(grid[0])
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    sum += 1
                if i == y - 1 or grid[i + 1][j] == 0:
                    sum += 1
                if j == 0 or grid[i][j - 1] == 0:
                    sum += 1
                if j == x - 1 or grid[i][j + 1] == 0:
                    sum += 1
        return sum
                    
if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
