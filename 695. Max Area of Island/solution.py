class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = list()
        r, c = len(grid), len(grid[0])
        for i in range(0, r):
            visited.append([False] * c)
            
        def BFS(i, j):  # grid[i][j] == 1
            s = 1
            nonlocal visited
            next = [(i, j)]
            island = [(i, j)]
            while len(next) > 0:
                new = list()
                for point in next:
                    if point[0] > 0 and grid[point[0] - 1][point[1]] \
                    and (point[0] - 1, point[1]) not in island:
                        new.append((point[0] - 1, point[1]))
                        s += 1
                        visited[point[0] - 1][point[1]] = True
                        island.append((point[0] - 1, point[1]))
                    if point[0] < r - 1 and grid[point[0] + 1][point[1]] \
                    and (point[0] + 1, point[1]) not in island:
                        new.append((point[0] + 1, point[1]))
                        s += 1
                        visited[point[0] + 1][point[1]] = True
                        island.append((point[0] + 1, point[1]))
                    if point[1] > 0 and grid[point[0]][point[1] - 1] \
                    and (point[0], point[1] - 1) not in island:
                        new.append((point[0], point[1] - 1))
                        s += 1
                        visited[point[0]][point[1] - 1] = True
                        island.append((point[0], point[1] - 1))
                    if point[1] < c - 1 and grid[point[0]][point[1] + 1] \
                    and (point[0], point[1] + 1) not in island:
                        new.append((point[0], point[1] + 1))
                        s += 1
                        visited[point[0]][point[1] + 1] = True
                        island.append((point[0], point[1] + 1))
                next = new
            return s
                
        res = 0
        for i in range(0, r):  # row index
            for j in range(0, c):  # column index
                if grid[i][j] and not visited[i][j]:
                    res = max(BFS(i, j), res)
                    
        return res
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
