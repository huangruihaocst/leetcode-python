class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # Solution 1: Brute Force

        # S = set(A)
        #
        # def max_length(m, n):  # try with first two items with m, n (m < n)
        #     nonlocal S
        #     res = 2
        #     while True:
        #         c = m + n
        #         if c in S:
        #             res += 1
        #             m, n = n, c
        #         else:
        #             return res
        #
        # ans = 0
        # for i in range(0, len(A)):
        #     for j in range(i + 1, len(A)):
        #         ans = max(ans, max_length(A[i], A[j]))
        # return ans if ans >= 3 else 0

        # Solution 2: Dynamic Programming
        indices = {val: i for i, val in enumerate(A)}
        from collections import defaultdict
        longest = defaultdict(lambda: 2)

        res = 0
        for k in range(1, len(A)):
            for j in range(k):
                pre = A[k] - A[j]
                i = indices.get(pre, None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    res = max(res, longest[j, k])
        return res if res >= 3 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
