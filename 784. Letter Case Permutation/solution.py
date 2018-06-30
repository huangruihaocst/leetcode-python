class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        from itertools import product
        ul = [S.lower(), S.upper()]
        res = set()
        for pro in product('01', repeat=len(S)):
            s = str()
            for i, val in enumerate(pro):
                s += ul[int(val)][i]
            res.add(s)
        return list(res)
            
if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))
