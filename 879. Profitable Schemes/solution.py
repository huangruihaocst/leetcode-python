class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # Solution 1: Dynamic Programming
        MOD = 10 ** 9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            for p1 in range(P + 1):
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                p2 = min(p1 + p0, P)
                for g1 in range(G - g0 + 1):
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD

        # Solution 2: DFS, Time Limit Exceeded (More test cases accepted with lru_cache :))
        # n = len(group)
        # from functools import lru_cache
        #
        # @lru_cache(None)
        # def DFS(g, p, i):
        #     nonlocal n
        #     if i == n:
        #         return 1 if p <= 0 else 0
        #     if group[i] <= g:
        #         return DFS(g - group[i], max(p - profit[i], 0), i + 1) + DFS(g, p, i + 1)
        #     else:
        #         return DFS(g, p, i + 1)
        #
        # return DFS(G, P, 0) % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
