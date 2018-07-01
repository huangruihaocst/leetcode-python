class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # Solution 1: Time Limit Exceeded
        # from itertools import product
        # from copy import deepcopy
        # row, col = len(A), len(A[0])
        # ans = 0
        # for toggles in product([True, False], repeat=row):
        #     AA = deepcopy(A)
        #     # toggle corresponding rows
        #     for i, r in enumerate(toggles):
        #         if r:
        #             AA[i] = list(map(lambda j: j ^ 1, AA[i]))
        #     s = 0
        #     for c in range(col):
        #         cnt = sum(AA[i][c] for i in range(row))
        #         s += max(cnt, row - cnt) * 2 ** (col - c - 1)
        #     ans = max(s, ans)
        # return ans
        
        # Solution 2: Accepted
        row, col = len(A), len(A[0])
        for r in range(0, row):
            A[r] = list(map(lambda j: j ^ A[r][0], A[r]))
        res = row * 2 ** (col - 1)
        for c in range(1, col):
            cnt = sum(A[i][c] for i in range(row))
            res += max(cnt, row - cnt) * 2 ** (col - c - 1)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
