class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1, N + 1):
        	digits = list()
        	while i > 9:
        		digits.append(i % 10)
        		i //= 10
        	digits.append(i)
        	if 3 in digits or 4 in digits or 7 in digits:
        		continue
        	if digits.count(0) + digits.count(1) + digits.count(8) == len(digits):
        		continue
        	res += 1
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.rotatedDigits(10))