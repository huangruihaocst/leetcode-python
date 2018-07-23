class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        res = 0
        for i in range(n):
            dist = dict()
            for j in range(n):
                d = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                dist[d] = dist[d] + 1 if d in dist else 1
            for k, v in dist.items():
                if v > 1:
                    res += (v - 1) * v

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
