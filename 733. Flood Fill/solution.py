class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, column = len(image), len(image[0])
        visit = [(sr, sc)]
        color = image[sr][sc]
        dye = list()
        while visit:
            new = list()
            for p in visit:
                if p not in dye:
                    dye.append(p)
                if p[0] > 0 and color == image[p[0] - 1][p[1]] and (p[0] - 1, p[1]) not in dye:  # up
                    new.append((p[0] - 1, p[1]))
                if p[0] < row - 1 and color == image[p[0] + 1][p[1]] and (p[0] + 1, p[1]) not in dye:  # down
                    new.append((p[0] + 1, p[1]))
                if p[1] > 0 and color == image[p[0]][p[1] - 1] and (p[0], p[1] - 1) not in dye:  # left
                    new.append((p[0], p[1] - 1))
                if p[1] < column - 1 and color == image[p[0]][p[1] + 1] and (p[0], p[1] + 1) not in dye:  # right
                    new.append((p[0], p[1] + 1))
            visit = new
        for p in dye:
            image[p[0]][p[1]] = newColor
        return image


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
