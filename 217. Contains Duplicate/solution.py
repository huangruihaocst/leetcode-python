class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))
