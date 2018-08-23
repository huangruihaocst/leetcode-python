class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b = sum(A), sum(B)
        delta = a - (a + b) // 2
        sb = set(B)
        for i in A:
            if i - delta in sb:
                return [i, i - delta]


if __name__ == '__main__':
    s = Solution()
    print(s.fairCandySwap([1, 2, 5], [2, 4]))

