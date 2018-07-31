class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        res = 0
        for val, cnt in counter.items():
            if val + 1 in counter:
                res = max(res, cnt + counter[val + 1])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
