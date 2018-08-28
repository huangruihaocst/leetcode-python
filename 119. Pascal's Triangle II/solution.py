class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev = [1, 1]
        while rowIndex > 1:
            new = [1]
            for i in range(1, len(prev)):
                new.append(prev[i - 1] + prev[i])
            new.append(1)
            prev = new
            rowIndex -= 1
        return prev


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))
