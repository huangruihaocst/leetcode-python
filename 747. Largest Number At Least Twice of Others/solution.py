class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Brute Force
        # m = max(nums)
        # if nums.count(m) > 1:
        #     return -1
        # for i in nums:
        #     if i != m and 2 * i > m:
        #         return -1
        # return nums.index(m)

        # Solution 2:
        # TODO


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex([1, 2, 3, 4]))
