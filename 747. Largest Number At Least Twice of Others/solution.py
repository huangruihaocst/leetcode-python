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
        big1, big2 = (-1, float('-inf')), (-1, float('-inf'))
        for i, v in enumerate(nums):
            if v > big1[1]:
                big2 = big1
                big1 = i, v
            elif v > big2[1]:
                big2 = i, v
        if big1[1] >= big2[1] * 2:
            return big1[0]
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex([3, 6, 1, 0]))
