class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        try:
            while True:
                nums.remove(0)
                cnt += 1
        except:
            for i in range(cnt):
                nums.append(0)
        
if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
    print(nums)
