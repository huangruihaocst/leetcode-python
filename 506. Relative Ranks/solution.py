class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums = sorted(nums, reverse=True)
        d = {v: i for i, v in enumerate(sorted_nums)}
        res = list()
        for v in nums:
            if d[v] == 0:
                res.append('Gold Medal')
            elif d[v] == 1:
                res.append('Silver Medal')
            elif d[v] == 2:
                res.append('Bronze Medal')
            else:
                res.append(str(d[v] + 1))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([5, 4, 3, 2, 1]))
