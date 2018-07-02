class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from itertools import combinations
        from math import sqrt
        res = 0
        for choice in combinations(range(len(points)), 3):
            A, B, C = points[choice[0]], points[choice[1]], points[choice[2]]
            # Solution 1:
            # AB = sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)
            # AC = sqrt((A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2)
            # BC = sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2)
            # if AB + AC <= BC or AB + BC <= AC or BC + AC <= AB:
            #     continue
            # q = (AB + AC + BC) / 2
            # S = sqrt(q * (q - AB) * (q - AC) * (q - BC))
            
            # Solution 2:
            S = 0.5 * abs((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]))    
            if S > res:
                res = S
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.largestTriangleArea([[4,6],[6,5],[3,1]]))
