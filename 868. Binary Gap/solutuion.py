class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        if b.count('1') < 2:
            return 0
        start = b.index('1')
        max, dis = 0, 0
        for i in range(start + 1, len(b)):
            dis += 1
            if b[i] == '1':
                if max < dis:
                    max = dis
                dis = 0
        return max

if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(6))
