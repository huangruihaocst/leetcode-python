class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        cnt = 0
        while z > 0:
            cnt += (z % 2)
            z = int(z / 2)
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
