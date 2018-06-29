class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        from math import log2
        digits = int(log2(num)) + 1
        return num ^ (2 ** digits - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
