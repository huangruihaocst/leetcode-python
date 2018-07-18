class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = list()
        curr, cnt = s[0], 1
        for i in s[1:]:
        	if i == curr:
        		cnt += 1
        	else:
        		cnts.append(cnt)
        		cnt = 1
        		curr = i
       	cnts.append(cnt)
        res = 0
        for i in range(len(cnts) - 1):
        	res += min(cnts[i], cnts[i + 1])
        return res


if __name__ == '__main__':
	s = Solution()
	print(s.countBinarySubstrings("00110011"))