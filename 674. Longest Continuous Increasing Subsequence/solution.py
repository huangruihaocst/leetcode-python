class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res, cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        res = max(res, cnt)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 7]))
