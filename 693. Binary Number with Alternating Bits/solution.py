class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1
        n >>= 1
        while n > 0:
            if last == n & 1:
                return False
            last = n & 1
            n >>= 1
        return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.hasAlternatingBits(5))
