class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max, cnt = 0, 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                if cnt > max:
                    max = cnt
                cnt = 0
        if cnt > max:
            max = cnt
        return max

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
