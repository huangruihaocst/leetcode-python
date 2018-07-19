class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
        	return a
        if a == 0:
            return b
        tmp = a ^ b
        b = (a & b) << 1
        a = tmp
        return self.getSum(a, b)


if __name__ == '__main__':
	s = Solution()
	print(s.getSum(5, 7))