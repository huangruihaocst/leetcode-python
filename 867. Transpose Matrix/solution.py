class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        res = list()
        for i in range(0, n):
            res.append(list())
            for j in range(0, m):
                res[i].append(A[j][i])
        return res
                
if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6]]))
