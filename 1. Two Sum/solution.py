class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            if target - v in d and d[target - v] != i:
                return [i, d[target - v]]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
