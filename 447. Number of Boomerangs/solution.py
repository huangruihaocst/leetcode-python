class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for [i, j] in points:
            dist = dict()
            for [x, y] in points:
                d = (i - x) * (i - x) + (j - y) * (j - y)
                dist[d] = dist[d] + 1 if d in dist else 1
            for k, v in dist.items():
                if v > 1:
                    res += (v - 1) * v

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
