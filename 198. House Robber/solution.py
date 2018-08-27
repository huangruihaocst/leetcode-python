class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1:
        # if not nums:
        #     return 0
        # res = float('-inf')
        # dp = list()
        # for i, v in enumerate(nums):
        #     if i < 2:
        #         tmp = v
        #     else:
        #         tmp = v + max(dp[:(i - 1)])
        #     res = max(res, tmp)
        #     dp.append(tmp)
        # return res

        # Solution 2:
        if not nums:
            return 0
        dp = list()
        for i, v in enumerate(nums):
            if i == 0:
                dp.append(nums[0])
            elif i == 1:
                dp.append(max(nums[:2]))
            else:
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
        return dp[len(nums) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
