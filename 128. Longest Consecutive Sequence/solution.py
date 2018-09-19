class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1:
        # from collections import defaultdict
        # d = defaultdict(lambda: 0)
        # res = 0
        # for i in nums:
        #     if d[i] == 0:
        #         update = d[i - 1] + d[i + 1] + 1
        #         d[i - d[i - 1]] = d[i + d[i + 1]] = d[i] = update
        #         res = max(res, update)
        # return res

        # Solution 2:
        _set = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in _set:  # i is the smallest of the consecutive sequence
                j = i + 1
                while j in _set:
                    j += 1
                res = max(res, j - i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
