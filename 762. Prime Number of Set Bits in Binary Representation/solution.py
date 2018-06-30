class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        cnt = 0
        for i in range(L, R + 1):
            ones = bin(i).count('1')
            if ones in primes:
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(10, 15))
