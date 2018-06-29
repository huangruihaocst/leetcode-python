class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list.sort(nums)
        sum = 0
        for i in range(0, len(nums) // 2):
            sum += nums[2 * i]
        return sum
        
if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1,4,3,2]))
