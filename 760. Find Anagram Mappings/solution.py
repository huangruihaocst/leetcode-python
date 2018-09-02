class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {v: i for i, v in enumerate(B)}
        res = list()
        for v in A:
            res.append(d[v])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
