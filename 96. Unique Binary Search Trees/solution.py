class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def num(size):
            if size < 2:
                return 1
            res = 0
            for i in range(1, size + 1):
                res += num(i - 1) * num(size - i)
            return res

        return num(n)


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))
