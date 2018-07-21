class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(area ** 0.5)
        while True:
            L = area / W
            if int(L) == L:
                return [int(L), W]
            else:
                W -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.constructRectangle(9999993))
