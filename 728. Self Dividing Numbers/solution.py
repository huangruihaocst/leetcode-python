class Solution:
    @staticmethod
    def decide(n):
        if n < 10:
            return True
        tmp = n
        while tmp > 0:
            if tmp % 10 == 0:
                return False
            else:
                if n % (tmp % 10) != 0:
                    return False
                else:
                    tmp = int(tmp / 10)
        return True
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = list()
        for n in range(left, right + 1):
            if self.decide(n):
                res.append(n)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1, 22))
