class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.invert(self.reverse(A))

    @staticmethod
    def reverse(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(lambda l: list(reversed(l)), A))

    @staticmethod
    def invert(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(lambda l: list(map(lambda i: 1 - i, l)), A))

if __name__ == '__main__':
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
