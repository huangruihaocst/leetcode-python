class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1:
        # sum_list = [0]
        # for i in nums:
        #     sum_list.append(sum_list[-1] + i)
        # curr_min = sum_list[0]
        # res = float('-inf')
        # for i in sum_list[1:]:
        #     res = max(res, i - curr_min)
        #     curr_min = min(curr_min, i)
        # return res

        # Solution 2:
        _max = nums[0]
        res = nums[0]
        for i in nums[1:]:
            _max = max(i, _max + i)
            res = max(res, _max)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
