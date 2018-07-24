class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_now = 0
        # d = dict()
        # for i in nums:
        #     d[i] = d[i] + 1 if i in d else 1
        #     max_now = max(max_now, d[i])
        from collections import Counter
        counter = Counter(nums)
        degree = max(counter.values())
        if degree == 1:
            return 1
        res = float('inf')
        reversed_nums = nums[::-1]
        for v, t in counter.items():
            if t == degree:
                first = nums.index(v)
                last = len(nums) - reversed_nums.index(v)
                res = min(res, last - first)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
