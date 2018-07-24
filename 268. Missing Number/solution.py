class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        s = n * (n - 1) // 2
        return s - sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
