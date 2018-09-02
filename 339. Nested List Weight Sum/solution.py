class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        res = 0

        def _sum(nlist, depth):
            nonlocal res
            for nl in nlist:
                if nl.isInteger():
                    res += depth * nl.getInteger()
                else:
                    _sum(nl.getList(), depth + 1)

        _sum(nestedList, 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.depthSum([1, [4, [6]]]))
